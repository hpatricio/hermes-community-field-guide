# Portable LLM Routing

- Ler `README.md` e `llm-routing/` antes de alterar.
- Este repositório é uma fonte portátil de capability, não um runtime Hermes completo.
- Nunca adicionar `.env`, tokens, auth, sessões, memória, state DB, logs, caches ou payloads privados.
- Começar por `plan`, `status` e `preflight`; são read-only.
- `apply` e `rollback` exigem `HERMES_ROUTING_APPLY=1`.
- Não alterar o modelo/provider diário por efeito implícito.
- Verificar os artefactos instalados depois de qualquer alteração.
