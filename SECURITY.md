# Security policy

## Scope

This repository contains public, unofficial documentation. It must not contain
API keys, OAuth tokens, passwords, session databases, raw transcripts, private
configuration, personal data, backups, logs or internal filesystem paths.

## Reporting a suspected exposure

Do not open a public issue with a secret or private payload. If a credential may
be exposed, stop using it and rotate or revoke it through the provider's normal
process. Then report the sanitized location and commit reference privately to
the repository maintainer through the contact method listed in the GitHub
profile, or use GitHub's private vulnerability-reporting flow if it is enabled.

If no private reporting channel is available, open a minimal issue containing
only the repository path, commit or URL, impact summary, and the fact that the
sensitive value has already been revoked. Never include the value itself.

## Contributor requirements

- inspect diffs before submission;
- redact secrets and personal data from examples;
- keep local evaluator exports and runtime state untracked;
- prefer placeholders such as `<REDACTED>` over realistic credentials;
- report whether a statement is official, observed, or community guidance.

This policy does not replace upstream Hermes security guidance or the security
policies of linked third-party projects.
