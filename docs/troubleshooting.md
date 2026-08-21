# Troubleshooting

Start with read-only checks. Do not reinstall or delete state before identifying the failure layer.

## First checks

```bash
hermes --version
hermes doctor
hermes status --all
hermes config check
```

Classify the failure:

1. launcher/install;
2. configuration;
3. authentication/provider;
4. model routing;
5. tool or skill loading;
6. gateway/platform;
7. project permissions or shell approval.

## Useful read-only commands

```bash
hermes --help
hermes chat --help
hermes skills check
hermes tools list
hermes logs errors
```

Use the command's current `--help` output when an article and the installed version disagree.

## Common boundaries

### Model/provider failure

A provider error is a route failure. Record the provider, model alias, HTTP status or error class and the fallback actually attempted. Do not claim Hermes itself is broken until the route has been isolated.

### Skill failure

Check the skill source and run the skill validator before changing runtime state. An installed skill can be stale, malformed or incompatible with the current Hermes version.

### Gateway failure

Separate gateway configuration, platform credentials, network reachability and model/provider health. A process being present is not proof that the gateway is ready.

### Permission/approval failure

Do not disable approvals globally as a first fix. Understand the command, scope and risk. Keep secret redaction enabled.

## Public bug report template

```text
Hermes version:
OS/platform:
Surface: CLI/TUI/desktop/dashboard/gateway
Provider/model class:
Command or action:
Observed output (redacted):
Expected behavior:
Read-only checks already run:
Reproduction steps:
```

Never include API keys, OAuth tokens, `auth.json`, `.env` contents, session transcripts, databases or private paths that reveal sensitive infrastructure.

## Official references

- [Hermes troubleshooting](https://hermes-agent.nousresearch.com/docs/)
- [Hermes repository issues](https://github.com/NousResearch/hermes-agent/issues)

Last reviewed: 2026-08-18
