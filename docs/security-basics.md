# Security basics

Hermes can run tools and interact with local state. Treat installation and configuration as an operational boundary, not as a cosmetic setup step.

## Never publish

- API keys, OAuth tokens or passwords;
- `.env` or `auth.json` contents;
- session databases and raw transcripts;
- backups, runtime databases or private logs;
- provider account identifiers when unnecessary;
- private Hermod/GinnungLabs configuration.

## Keep the safe defaults

Hermes secret redaction is enabled by default in the current guidance. Keep it enabled unless deliberately debugging a controlled redaction test.

Command approvals, secret redaction and PII redaction are separate controls. Disabling one does not disable the others.

## Before installing a third-party skill or plugin

1. identify the owner and repository;
2. inspect the license and recent activity;
3. read scripts before running them;
4. check requested paths, network calls and environment variables;
5. use a disposable profile or test environment where possible;
6. avoid granting more access than the task requires;
7. record the version or commit used.

## Reporting a problem

Use a redacted reproduction. If the issue may expose a secret, stop, rotate the credential through the provider's normal process and do not attach the original output.

For detailed behavior, use the [official Hermes security and configuration documentation](https://hermes-agent.nousresearch.com/docs/).

Last reviewed: 2026-08-18
