# Workshop 02 - Data Quality

Para desenvolver o desafio de negocio, vamos montar a seguinte ETL

## Fluxo

```mermaid
graph TD;
    A[Configura Variáveis] --> B[Ler o Banco SQL];
    B --> V[Validação do Schema de Entrada];
    V -->|Falha| X[Alerta de Erro];
    V -->|Sucesso| C[Transformar os KPIs];
    C --> Y[Validação do Schema de Saída];
    Y -->|Falha| Z[Alerta de Erro];
    Y -->|Sucesso| D[Salvar no DuckDB];
```

# Contrato de dados

::: app.schema.ProdutoSchema

# Transformacoes

## Configura Variáveis

::: app.etl.load_settings

## Ler o Banco SQL
::: app.etl.extrair_do_sql

## Transformar os KPIs

::: app.etl.transformar

## Salvar no DuckDB
S
::: app.etl.load_to_duckdb
