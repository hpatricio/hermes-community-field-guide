#!/usr/bin/env python3
"""Offline, deterministic model selection. Never reads credentials or uses network."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
BOOLS = ("tool_call", "structured_output", "reasoning", "open_weights")
def number(value, default=None):
    try: return float(value)
    except (TypeError, ValueError): return default
def load_catalog(path):
    catalog = json.loads(Path(path).read_text())
    models = catalog.get("models", []) if isinstance(catalog, dict) else catalog
    if not isinstance(models, list): raise SystemExit("catalog models must be an array")
    return catalog, models
def name(model): return str(model.get("name", model.get("model_name", "")))
def matches(model, req):
    for key in BOOLS:
        if req.get(key) is True and model.get(key) is not True: return False
    for key in ("intelligence", "coding", "math", "context_window"):
        minimum = number(req.get("min_" + key))
        if minimum is not None and number(model.get(key), -math.inf) < minimum: return False
    return True
def price(model):
    direct = number(model.get("price"))
    if direct is not None: return max(direct, 0.0)
    return (number(model.get("input_price"), 0.0) + number(model.get("output_price"), 0.0)) / 2
def score(model, weights):
    quality = number(model.get("intelligence"), 0.0) / 100.0
    coding = number(model.get("coding"))
    if coding is not None: quality = (quality + coding / 100.0) / 2
    cost = 1.0 / (1.0 + price(model)); speed = min((number(model.get("tps"), 0.0) or 0.0) / 200.0, 1.0)
    return round(quality * weights["quality"] + cost * weights["cost"] + speed * weights["speed"], 6)
def provenance(catalog):
    return catalog.get("provenance", {"sourceType":"reference-only", "sourceRevision":None, "capturedAt":None, "evidenceStatus":"not_validated"}) if isinstance(catalog, dict) else {"sourceType":"reference-only", "evidenceStatus":"not_validated"}
def main():
    p = argparse.ArgumentParser(); p.add_argument("--mode", choices=("select", "compare", "cost"), default="select"); p.add_argument("--request"); p.add_argument("--catalog", required=True); p.add_argument("--output", required=True); p.add_argument("--names", nargs="*"); p.add_argument("--model"); p.add_argument("--input-tokens", type=float, default=0); p.add_argument("--output-tokens", type=float, default=0); p.add_argument("--requests", type=float, default=1); p.add_argument("--period", default="request"); a = p.parse_args()
    catalog, models = load_catalog(a.catalog); by_name = {name(m).lower(): m for m in models}
    if a.mode == "select":
        if not a.request: raise SystemExit("--request is required for select")
        request = json.loads(Path(a.request).read_text()); req = request.get("requirements", {}); raw = request.get("priority", {"quality": .4, "cost": .4, "speed": .2}); total = sum(float(raw.get(k, 0)) for k in ("quality", "cost", "speed")) or 1.0; weights = {k: float(raw.get(k, 0)) / total for k in ("quality", "cost", "speed")}; ranked = [{**m, "selectionScore": score(m, weights)} for m in models if matches(m, req)]; ranked.sort(key=lambda m: (-m["selectionScore"], name(m))); result = {"schemaVersion":"0.1.0", "taskClass":request.get("taskClass", "unspecified"), "primary":ranked[0] if ranked else None, "fallback":ranked[1:3], "shortlist":ranked[:5], "provenance":provenance(catalog), "validation":{"status":"candidate" if ranked else "blocked", "activationAllowed":False, "reason":"shortlist only; local workload and runtime validation required"}}
    elif a.mode == "compare":
        wanted = [n.lower() for n in (a.names or [])]; selected = [by_name[n] for n in wanted if n in by_name]; result = {"models":selected, "missing":[n for n in wanted if n not in by_name], "provenance":provenance(catalog), "validation":{"status":"candidate", "activationAllowed":False}}
    else:
        if not a.model: raise SystemExit("--model is required for cost")
        model = by_name.get(a.model.lower())
        if model is None: raise SystemExit("model not found")
        per_request = (a.input_tokens * number(model.get("input_price"), price(model)) + a.output_tokens * number(model.get("output_price"), price(model))) / 1_000_000; result = {"model":model, "inputTokens":a.input_tokens, "outputTokens":a.output_tokens, "requests":a.requests, "period":a.period, "costPerRequest":round(per_request, 8), "projectedCost":round(per_request * a.requests, 8), "currency":"USD", "provenance":provenance(catalog), "validation":{"status":"candidate", "activationAllowed":False}}
    Path(a.output).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
if __name__ == "__main__": main()
