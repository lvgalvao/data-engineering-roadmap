import csv

from pydantic import validate_call

@validate_call
def ler_csv_para_transformar_em_um_dict(path: str) -> list[dict]:
    dados = []
    with open(file=path, mode="r", encoding="utf-8") as file:
        leitor_csv = csv.DictReader(file)
        for linha in leitor_csv:
            # Adiciona cada linha (um dicionário) à lista de dados
            dados.append(linha)
    return dados

@validate_call
def filtra_produtos_entregues(lista = list[dict]) -> list[dict]:
    lista_de_produtos_entregues = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_de_produtos_entregues.append(produto)
    return lista_de_produtos_entregues

@validate_call
def somar_valores(lista = list[dict]) -> int:
    valor_total = 0
    for produto in lista:
        valor_total += int(produto.get("price"))
    return valor_total

@validate_call
def pipeline(path: str):
    lista_de_produtos = ler_csv_para_transformar_em_um_dict(path)
    produtos_entregues = filtra_produtos_entregues(lista_de_produtos)
    return somar_valores(produtos_entregues)




