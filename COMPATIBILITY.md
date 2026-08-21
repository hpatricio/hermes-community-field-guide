# Compatibility and review record

This guide is an unofficial documentation layer. Upstream Hermes Agent and its
[official documentation](https://hermes-agent.nousresearch.com/docs/) remain
the authority when commands or behavior differ.

## Public release baseline

- Guide release: `0.1.0`
- Review date: 2026-08-21 (UTC)
- Repository type: documentation-only Markdown repository
- Tested surface: static files, relative links, Git history exposure checks and
  GitHub unauthenticated retrieval
- Provider credentials: none are required or included

## How to interpret examples

- **Official** means linked directly to upstream documentation or source.
- **Observed** means tested against a declared local environment; this release
  does not claim a complete Hermes runtime compatibility matrix.
- **Community guidance** is a practical recommendation, not an upstream
  guarantee.
- **Unverified** items must be checked against the installed version with
  `hermes --help` and the current official documentation.

## Maintenance

Review commands and external links before each release. When upstream behavior
changes, update the affected page, record the review date, and describe the
change in `CHANGELOG.md`. Do not add credentials, private runtime state,
internal filesystem paths or raw evaluator output as compatibility evidence.
