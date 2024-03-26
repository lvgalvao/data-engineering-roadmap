from pydantic import BaseModel, field_validator, ValidationError
from typing import List, Dict, Optional
import csv

class ItemVenda(BaseModel):
    Produto: str
    Categoria: str
    Quantidade: int
    Venda: int

    # Validador para garantir valores positivos
    @field_validator('Quantidade', 'Venda')
    def valores_positivos(cls, v):
        assert v >= 0, 'deve ser positivo'
        return v

class CategoriaDados(BaseModel):
    Categoria: str
    Itens: List[ItemVenda]
    TotalVendas: Optional[int] = 0

    def calcular_total_vendas(self):
        self.TotalVendas = sum(item.Quantidade * item.Venda for item in self.Itens)

def ler_csv(nome_arquivo: str) -> List[ItemVenda]:
    dados_validados = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            try:
                item = ItemVenda(**linha)
                dados_validados.append(item)
            except ValidationError as e:
                print(f"Erro de validação: {e.json()}")
    return dados_validados

def processar_dados(dados: List[ItemVenda]) -> Dict[str, CategoriaDados]:
    categorias = {}
    for item in dados:
        if item.Categoria not in categorias:
            categorias[item.Categoria] = CategoriaDados(Categoria=item.Categoria, Itens=[])
        categorias[item.Categoria].Itens.append(item)
    return categorias

def calcular_vendas_categoria(dados: Dict[str, CategoriaDados]) -> Dict[str, int]:
    vendas_por_categoria = {}
    for categoria, dados_categoria in dados.items():
        dados_categoria.calcular_total_vendas()
        vendas_por_categoria[categoria] = dados_categoria.TotalVendas
    return vendas_por_categoria

def main():
    nome_arquivo = 'vendas.csv'
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f'{categoria}: ${total}')

if __name__ == '__main__':
    main()