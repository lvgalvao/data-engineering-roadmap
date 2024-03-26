import csv
from typing import List, Dict

# Função para ler o arquivo CSV
def ler_csv(nome_arquivo: str) -> List[Dict[str, str]]:
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

# Função para processar os dados em um dicionário
def processar_dados(dados: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

# Função para calcular o total de vendas por categoria
def calcular_vendas_categoria(dados: Dict[str, List[Dict[str, str]]]) -> Dict[str, int]:
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

# Função principal para integrar as funções anteriores
def main():
    nome_arquivo = 'vendas.csv'
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()
