import csv

# Caminho para o arquivo CSV
caminho_arquivo = 'exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)