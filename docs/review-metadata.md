# Review metadata and compatibility

This page records the evidence behind the guide. It is not a compatibility promise.

## Current review

| Field | Value |
|---|---|
| Review date | 2026-08-21 (UTC) |
| Guide status | Public community release (`0.1.0`) |
| Hermes version | Not verified in a live Hermes installation |
| Host tested | Linux audit environment; no runtime command validation claimed |
| Surfaces tested | Documentation structure, local links, tracked-history scan and public retrieval |
| Provider | No provider credentials or live route used |
| Evidence boundary | Official links are authoritative; commands in this guide remain community guidance until rechecked |

The repository is documentation-only. The review covered tracked Markdown, relative-link integrity, repository state and publication-boundary risks. It did not prove that every command works on every Hermes version, operating system, provider or surface.

## How to read labels

- **Official** — points to current upstream documentation or source.
- **Observed** — exercised against the version and environment named here.
- **Community guidance** — a practical recommendation that is not an upstream guarantee.
- **Unverified** — retained as a lead until a maintainer records reproducible evidence.

## Maintainer update procedure

When validating a command, record the Hermes version, OS, surface, provider class (never credentials), command, result and date. Prefer read-only checks first. If upstream behavior changes, update the affected page and changelog entry together; do not silently preserve stale instructions.

## Release gates

- [x] Resolve private authenticated distribution versus public publication.
- [x] Add a license for original documentation.
- [ ] Recheck command examples against the current upstream `--help` and official docs.
- [x] Remove private companion links from the public guide.
- [x] Keep evaluator exports and local audit evidence out of Git.

Last reviewed: 2026-08-21
