# Skills and extensions

Hermes skills are reusable procedures loaded into future sessions. They are not the same thing as plugins, MCP servers or provider configuration.

## Discover installed skills

```bash
hermes skills list
hermes skills browse
hermes skills search "your topic"
```

## Inspect and install

Inspect a skill before trusting it. A skill can contain instructions, scripts and references, so review its provenance and scope.

```bash
hermes skills inspect <id>
hermes skills install <id-or-https-url>
hermes skills check
```

A direct `SKILL.md` URL should come from a repository or publisher you trust. Do not install a skill merely because its name looks official.

## Community skill sources

Hermes can add a repository as a skill source:

```bash
hermes skills tap add <owner/repository>
```

Treat tapped repositories as external sources. Check the repository owner, license, recent changes, scripts and requested permissions before installing anything.

## Skill safety checklist

- [ ] source and owner are known;
- [ ] license and publication state are clear;
- [ ] the skill does not request secrets unnecessarily;
- [ ] scripts are read before execution;
- [ ] paths and external integrations are bounded;
- [ ] the skill does not override project instructions silently;
- [ ] the installed copy can be removed or disabled.

## Skills, plugins and MCP are different

- **Skill:** reusable instructions and procedures.
- **Plugin:** runtime extension that can add tools, commands or UI behavior.
- **MCP server:** external tool/resource provider connected through MCP.
- **Provider:** model or service route used by Hermes.

A guide or catalog should not call a community plugin “safe” without inspecting and testing it.

## Official references

- [Hermes skills catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog)
- [Hermes repository](https://github.com/NousResearch/hermes-agent)

Last reviewed: 2026-08-18
