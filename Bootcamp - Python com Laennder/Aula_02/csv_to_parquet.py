import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('vendas.csv')

# Salvando o DataFrame como arquivo Parquet
df.to_parquet('vendas.parquet')
