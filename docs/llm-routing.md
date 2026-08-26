# Portable LLM routing package

This repository includes a small, provider-neutral package for optionally adding bounded LLM routing utilities to an independent Hermes installation.

## What it provides

- offline, deterministic model selection from reference-only catalogues;
- candidate comparison and cost projection;
- read-only environment preflight;
- a credential-free LiteLLM/Ollama reference configuration;
- an optional Hermes skill;
- an explicit installer that writes only to `$HERMES_HOME/llm-routing`.

Package source: [`packages/llm-routing-export/README.md`](../packages/llm-routing-export/README.md)

## Install

Download the repository archive or release artifact, then run:

```bash
cd packages/llm-routing-export
./install-hermes.sh plan
./install-hermes.sh status
HERMES_ROUTING_APPLY=1 ./install-hermes.sh apply
```

The installer does not install Ollama/LiteLLM, start services, read credentials,
or change the Hermes default model. Review `README.md` in the package before
using it. Activation of any provider route is a separate, explicit operation.

The package is community-maintained and unofficial. Hermes Agent's upstream
source and [official documentation](https://hermes-agent.nousresearch.com/docs/)
remain authoritative.

Last reviewed: 2026-08-26
