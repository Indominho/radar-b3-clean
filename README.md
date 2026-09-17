# Radar B3 IA Clean

Versão limpa do Radar B3, sem reaproveitar `ranking.json` antigo.

## Regras

- Um único workflow de atualização e publicação.
- Catálogo completo gerado diariamente a partir da fonte configurada.
- Indicadores mostram valor, fonte e data; nunca inventam números.
- Histórico insuficiente fica identificado e não contamina rankings de outro período.
- Cada release incrementa `VERSION.json`.

## Publicação

GitHub Pages usa exclusivamente `.github/workflows/publish.yml`.
