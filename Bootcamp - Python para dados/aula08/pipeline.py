from etl import pipeline
from pathlib import Path

if __name__ == "__main__":
    # Define as pastas de entrada e saída usando pathlib
    pasta_raiz = Path(__file__).parent
    pasta_entrada = pasta_raiz / 'data'

    formato_saida = ["csv"]  # Ou 'parquet', conforme a decisão de saída

    pipeline(pasta_entrada, formato_saida)
