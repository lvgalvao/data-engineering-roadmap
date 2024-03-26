import pandas as pd

class ProcessadorCSV:
    def __init__(self, arquivo_csv):
        self.arquivo_csv = arquivo_csv
        self.df = None
    
    def carregar_csv(self):
        # Carregar o arquivo CSV em um DataFrame
        self.df = pd.read_csv(self.arquivo_csv)
    
    def remover_celulas_vazias(self):
        # Verificar e remover células vazias
        self.df = self.df.dropna()
    
    def filtrar_por_estado(self, estado):
        # Filtrar as linhas pela coluna estado
        self.df = self.df[self.df['estado'] == estado]
    
    def processar(self, estado):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)
        
        return self.df

# Exemplo de uso
arquivo_csv = './exemplo.csv'  # substitua 'exemplo.csv' pelo caminho do seu arquivo CSV
estado_filtrado = 'SP'  # estado que você quer filtrar

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar(estado_filtrado)

print(df_filtrado)
