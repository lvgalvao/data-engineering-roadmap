import pandas as pd
import glob
import os
import pandera as pa
from schema import VendasSchema
from pathlib import Path

def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(df_total)
    return df_total

def transformar_dados(df: pd.DataFrame):
    df['Receita'] = df['Quantidade'] * df['Venda']
    print(df)
    return df

def carregar_dados(df: pd.DataFrame, caminho_saida: str, formatos: list):
    caminho_saida_path = Path(caminho_saida)  # Converte a string de caminho em um objeto Path

    # Garante que o diretório de saída existe
    caminho_saida_path.mkdir(parents=True, exist_ok=True)

    for formato in formatos:
        if formato == 'csv':
            caminho_completo = caminho_saida_path / "dados.csv"
            df.to_csv(caminho_completo, index=False)
        elif formato == 'parquet':
            caminho_completo = caminho_saida_path / "dados.parquet"
            df.to_parquet(caminho_completo, index=False)

def pipeline(pasta_entrada: str, caminho_saida: str, formato_saida: str):
    dados = extrair_dados(pasta_entrada)
    dados_transformados = transformar_dados(dados)
    carregar_dados(dados_transformados, caminho_saida, formato_saida)