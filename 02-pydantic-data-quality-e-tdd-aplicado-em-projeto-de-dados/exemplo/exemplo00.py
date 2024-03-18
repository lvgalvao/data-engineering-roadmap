from pydantic import BaseModel, PositiveFloat, PositiveInt

dados = {
    "id_produto": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "nome": ["Produto A", "Produto B", "Produto C", "Produto D", "Produto E", 
             "Produto F", "Produto G", "Produto H", "Produto I", "Produto J"],
    "quantidade": [100, 150, 200, 50, 120, 80, 60, 30, 90, 20],
    "preco": [10.0, 20.0, 15.0, 5.0, 22.0, 45.0, 120.0, 85.0, 55.0, 100.0],
    "categoria": ["eletronicos", "mobilia", "informatica", "decoracao", "eletronicos", 
                  "mobilia", "informatica", "decoracao", "eletronicos", "mobilia"]
}

class SchemaDados(BaseModel):
    id_produto: int
    nome: str
    quantidade: PositiveInt
    preco: PositiveFloat
    categoria: str