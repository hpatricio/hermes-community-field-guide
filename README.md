# Hermes Community Field Guide

Unofficial, practical guidance for installing, configuring and using [Hermes Agent](https://github.com/NousResearch/hermes-agent).

> This repository is **not** an official Hermes Agent project. The upstream repository and [official documentation](https://hermes-agent.nousresearch.com/docs/) remain authoritative. Commands and provider behavior can change; each page records its review date.

## Start here

New to Hermes? Follow this order:

1. [Installation and first setup](docs/installation.md) — a bounded first-run checklist.
2. [Skills and extensions](docs/skills.md) — distinguish skills, plugins, MCP and providers.
3. [Troubleshooting](docs/troubleshooting.md) — classify failures before changing state.
4. [Security basics](docs/security-basics.md) — keep credentials and private runtime data out of reports.
5. [Community resources](docs/community-resources.md) — curated links, not endorsements.

Maintainers and contributors should also read [review metadata](docs/review-metadata.md), [compatibility record](COMPATIBILITY.md), [contributing](CONTRIBUTING.md) and [security policy](SECURITY.md).

## Current status

This is a public, unofficial community guide. The original documentation is
licensed under [CC BY 4.0](LICENSE); upstream and third-party material remains
subject to its own terms. Private evaluator exports and private companion
projects are deliberately excluded from the public surface.

## Validate locally

This repository is documentation-only. Run the bounded local checks before proposing a change:

```bash
python3 scripts/check-docs.py
git diff --check
```

## What this guide is

- a short onboarding layer over the official documentation;
- practical examples and checklists;
- a curated index of community resources;
- a place to report instructions that are stale or unclear.

## What this guide is not

- a replacement for the Hermes source repository or official docs;
- a promise of compatibility with every provider, platform or plugin;
- a support service;
- a copy of private Hermod or GinnungLabs runtime state.

## Review policy

Every page should distinguish:

- **Official:** directly linked to Hermes documentation or source;
- **Observed:** tested against a declared Hermes version/environment;
- **Community guidance:** a practical recommendation, not an upstream guarantee;
- **Unverified:** a lead that still needs testing.

Review date: 2026-08-21

## Support

If this guide saves you time, you can support its maintenance through [GitHub Sponsors](https://github.com/sponsors/hpatricio). Sponsorship is voluntary and does not provide priority support or guaranteed compatibility.
