from datetime import date

class Venda:
    def __init__(self, id: int, produto: str, valor: float, quantidade: int, data: date, email_comprador: str):
        self.id: int = id
        self.produto: str = produto
        self.valor: float = valor
        self.quantidade: int = quantidade
        self.data: date = data
        self.email_comprador: str = email_comprador

    def __repr__(self) -> str:
        return f"Venda(id={self.id}, produto={self.produto}, valor={self.valor}, quantidade={self.quantidade}, data={self.data}, email_comprador={self.email_comprador})"

# Exemplo de uso
venda = Venda(1, "Notebook Gamer", 5000.00, 2, date(2024, 3, 18), "cliente@example.com")
print(venda)
