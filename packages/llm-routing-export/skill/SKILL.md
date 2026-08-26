---
name: portable-llm-routing
description: Use when selecting or evaluating LLM routes in a Hermes installation.
version: 0.1.0
---

# Portable LLM routing

Use the files under `$HERMES_HOME/llm-routing` as optional, reference-only routing utilities.

- Start with `preflight.py` and offline `model-selection.py`.
- Treat catalog values as evidence, not proof of workload quality.
- Keep credentials in Hermes/provider-managed secret storage; never put them in the package.
- Small local models are bounded transformers: invoke them without Hermes tools when appropriate.
- A recommendation is not an active route.
- Do not change the daily/default model implicitly.
- Before activation, validate real provider IDs, auth, streaming, retries, latency, cost, quality and fallback.
