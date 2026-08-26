# Portable LLM Routing for Hermes

Pacote autónomo para uma instalação Hermes independente. Fornece:

- selecção offline e determinística de modelos a partir de um catálogo de evidência;
- comparação de candidatos;
- estimativa de custo;
- configuração de referência para LiteLLM + Ollama;
- preflight read-only;
- skill opcional para orientar o Hermes.

## Limites

Este pacote **não** contém credenciais, tokens, sessões, memória, bases de dados, logs ou payloads privados. Não activa providers, não altera o modelo diário e não substitui o runtime Hermes. O catálogo incluído é uma fixture de teste, não uma recomendação actual.

A instalação escreve apenas em `$HERMES_HOME/llm-routing` (por defeito `~/.hermes/llm-routing`). O valor `HERMES_HOME` deve apontar para a instalação/perfil pretendido.

## Instalação

```bash
./install-hermes.sh plan
./install-hermes.sh status
./install-hermes.sh apply
```

`apply` requer `HERMES_ROUTING_APPLY=1` e faz backup da instalação anterior fora do pacote. Para remover apenas os artefactos instalados:

```bash
HERMES_ROUTING_APPLY=1 ./install-hermes.sh rollback
```

A instalação não instala LiteLLM/Ollama nem inicia serviços. Esses passos dependem do sistema do destinatário e devem ser decididos separadamente.

## Utilização

```bash
python3 llm-routing/model-selection.py --mode select \
  --request llm-routing/fixtures/selection-request.json \
  --catalog llm-routing/fixtures/model-catalog.json \
  --output /tmp/model-selection.json

python3 llm-routing/model-selection.py --mode compare \
  --names cheap-tool strong-tool missing \
  --catalog llm-routing/fixtures/model-catalog.json \
  --output /tmp/model-compare.json

python3 llm-routing/model-selection.py --mode cost --model cheap-tool \
  --input-tokens 10000 --output-tokens 2000 --requests 100 \
  --catalog llm-routing/fixtures/model-catalog.json \
  --output /tmp/model-cost.json
```

## Integração opcional

`llm-routing/litellm.config.yaml` é uma configuração de referência sem secrets. Rever modelos, endpoints, limites e fallback antes de usar. Se for necessário expor aliases ao Hermes, usar os comandos oficiais `hermes config set` no perfil correcto, após validar o endpoint e com aprovação do operador. Não assumir que um alias LiteLLM é automaticamente resolvido pelo Hermes.

## Proveniência

O selector é uma adaptação genérica de um padrão de selecção baseado em evidência. A fixture regista a revisão de referência; os seus números não são uma medição do workload do destinatário. Para promoção de uma rota: validar provider/model IDs reais, auth, streaming, timeout/retry, custo, latência, qualidade e fallback.
