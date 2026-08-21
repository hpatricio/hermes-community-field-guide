# Contributing

This repository is an unofficial community guide. Contributions should improve practical clarity without pretending to be upstream Hermes documentation.

Before opening a change:

- link to the official source when describing Hermes behavior;
- state the Hermes version or review date when relevant;
- do not include secrets, private runtime state or raw transcripts;
- distinguish observed behavior from community recommendation;
- keep changes narrow and reproducible.

Before opening an issue, read [SECURITY.md](SECURITY.md). Never include secrets or private runtime material in a public report.

Run the local checks from the repository root:

```bash
python3 scripts/check-docs.py
git diff --check
```

For upstream Hermes bugs or feature requests, use the [upstream issue tracker](https://github.com/NousResearch/hermes-agent/issues) instead. This guide cannot promise upstream support or compatibility.
