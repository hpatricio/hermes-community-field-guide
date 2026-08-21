#!/usr/bin/env python3
"""Bounded checks for this documentation-only repository."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
files = sorted(ROOT.rglob("*.md"))
errors = []
secret_patterns = [
    re.compile(r"-----BEGIN (?:OPENSSH|RSA|EC|PGP) PRIVATE KEY-----"),
    re.compile(r"(?:api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-/+=]{20,}", re.I),
]
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
for path in files:
    text = path.read_text(encoding="utf-8")
    if "\t" in text:
        errors.append(f"{path.relative_to(ROOT)}: tab character")
    for pattern in secret_patterns:
        if pattern.search(text):
            errors.append(f"{path.relative_to(ROOT)}: possible secret pattern")
    for target in link_re.findall(text):
        target = target.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.is_file():
            errors.append(f"{path.relative_to(ROOT)}: broken local link {target}")

if errors:
    print("Documentation checks failed:")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)
print(f"Documentation checks passed: {len(files)} Markdown files, local links resolved.")
