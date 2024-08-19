import csv 
from typing import List, Dict
import pandas as pd

def ler_csv(path: str) -> List:
    with open(path, mode = 'r', encoding= 'utf-8') as file: 
        reader = csv.DictReader(file)
        return list(reader)
    
def processar_dados(lista_dict: List[dict]) -> Dict: 
    produtos = []
    quantidades = []
    vendas = []
    for i in range(len(lista_dict)):
        produtos.append(lista_dict[i]['Produto'])
        quantidades.append(lista_dict[i]['Quantidade'])
        vendas.append(lista_dict[i]['Venda'])
    
    return {'Produto': produtos, 'Quantidade': quantidades, 'Venda': vendas}

def somar_valores(dicionario: Dict) -> List[float]:
    totais: List =[] 

    for i in range(len(dicionario['Produto'])):
        quantidade: int = int(dicionario['Quantidade'][i])
        venda: int = int(dicionario['Venda'][i])
        total = quantidade * venda 
        totais.append(total)
    
    dicionario['Total'] = totais

    return dicionario

def ler_DataFrame(dicionario_valores_categoria: Dict) -> pd.DataFrame:
    df = pd.DataFrame(dicionario_valores_categoria) 
    print(df)

dicionario_csv: Dict = ler_csv('./vendas.csv')
dicionario_processado: Dict = processar_dados(dicionario_csv)
dicionario_valores_categoria: List = somar_valores(dicionario_processado)
print(dicionario_valores_categoria)
ler_DataFrame(dicionario_valores_categoria)