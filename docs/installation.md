# Installation and first setup

This is a short community checklist. For the authoritative installation path, use the [official Hermes documentation](https://hermes-agent.nousresearch.com/docs/) and the upstream [Hermes Agent repository](https://github.com/NousResearch/hermes-agent).

## 1. Install

Use the official installer or the installation method documented upstream. Do not copy API keys into shell history or public issue reports.

After installation, confirm that the launcher is available:

```bash
hermes --version
hermes doctor
```

If the command is not found, stop and follow the current upstream installation troubleshooting rather than guessing a PATH fix.

## 2. Configure the first model/provider

Use the interactive setup or model selector:

```bash
hermes setup
hermes model
```

Keep provider credentials in Hermes' protected runtime configuration. Settings belong in `config.yaml`; secrets belong in the protected environment/auth store. Never commit `.env`, `auth.json`, tokens, session databases or provider credentials.

## 3. Run a first bounded query

```bash
hermes chat -q "Reply with exactly: HERMES_OK"
```

Then run a harmless query with the intended tools disabled or restricted. This confirms the model route before attempting integrations.

## 4. Check the local state safely

```bash
hermes status --all
hermes config check
```

Do not paste full configuration output into public issues: it may contain paths, account identifiers or provider metadata.

## 5. First acceptance checklist

- [ ] `hermes --version` returns a version;
- [ ] `hermes doctor` completes or reports a specific blocker;
- [ ] a model/provider is configured;
- [ ] one bounded query succeeds;
- [ ] secrets are outside Git;
- [ ] the user understands which surface is being used: CLI, TUI, desktop, dashboard or gateway.

## Version note

This page is a community checklist, not a promise that every command remains unchanged. Before following a command copied from an older issue or article, compare it with `hermes --help` and the current official docs.

Last reviewed: 2026-08-18
