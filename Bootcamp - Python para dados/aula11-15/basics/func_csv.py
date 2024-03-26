import pandas as pd


def carregar_csv_e_filtrar(arquivo_csv, estado):
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(arquivo_csv)
    
    # Verificar e remover células vazias
    df = df.dropna()
    
    # Filtrar as linhas pela coluna estado
    df_filtrado = df[df['estado'] == estado]
    
    return df_filtrado

arquivo_csv = './exemplo.csv'  # substitua 'dados.csv' pelo caminho do seu arquivo CSV
estado_filtrado = 'SP'  # estado que você quer filtrar
df_filtrado = carregar_csv_e_filtrar(arquivo_csv, estado_filtrado)

print(df_filtrado)