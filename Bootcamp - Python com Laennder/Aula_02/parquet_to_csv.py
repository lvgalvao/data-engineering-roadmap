import pandas as pd

# Leitura do arquivo Parquet
df = pd.read_parquet('vendas.parquet')

# Salvando o DataFrame como arquivo CSV
df.to_csv('vendas.csv', index=False)
