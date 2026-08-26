#!/usr/bin/env bash
set -Eeuo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
HERMES_HOME="${HERMES_HOME:-$HOME/.hermes}"
DEST="${HERMES_HOME}/llm-routing"
MODE="${1:-status}"
case "$MODE" in plan|status|apply|rollback) ;; *) printf 'usage: %s {plan|status|apply|rollback}\n' "$0"; exit 64;; esac
case "$MODE" in
  plan) printf 'target=%s\nmode=plan\ncredentials=not-read\nservices=not-started\n' "$DEST"; exit 0;;
  status) if [[ -f "$DEST/manifest.json" ]]; then printf 'installed=%s\n' "$DEST"; else printf 'installed=no\ntarget=%s\n' "$DEST"; fi; exit 0;;
  rollback) [[ "${HERMES_ROUTING_APPLY:-0}" == 1 ]] || { printf 'rollback requires HERMES_ROUTING_APPLY=1\n' >&2; exit 77; }; rm -rf "$DEST"; printf 'removed=%s\n' "$DEST"; exit 0;;
  apply) [[ "${HERMES_ROUTING_APPLY:-0}" == 1 ]] || { printf 'apply requires HERMES_ROUTING_APPLY=1\n' >&2; exit 77; }; mkdir -p "$HERMES_HOME"; if [[ -e "$DEST" ]]; then mv "$DEST" "${DEST}.backup.$(date -u +%Y%m%dT%H%M%SZ)"; fi; mkdir -p "$DEST"; cp -R "$HERE/llm-routing"/. "$DEST/"; cp "$HERE/README.md" "$HERE/AGENTS.md" "$DEST/"; printf 'installed=%s\nmodel_default=unchanged\nprovider_auth=untouched\n' "$DEST";;
esac
