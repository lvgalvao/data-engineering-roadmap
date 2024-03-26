import re
from datetime import date

class VendaValidada:
    def __init__(self, id: int, produto: str, valor: float, quantidade: int, data: date, email_comprador: str):
        if not isinstance(valor, float) or valor <= 0:
            raise ValueError("Valor deve ser um float positivo.")
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("Quantidade deve ser um int positivo.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_comprador):
            raise ValueError("E-mail do comprador inválido.")

        self.id: int = id
        self.produto: str = produto
        self.valor: float = valor
        self.quantidade: int = quantidade
        self.data: date = data
        self.email_comprador: str = email_comprador

    def __repr__(self) -> str:
        return f"VendaValidada(id={self.id}, produto={self.produto}, valor={self.valor}, quantidade={self.quantidade}, data={self.data}, email_comprador={self.email_comprador})"

# Exemplo de uso
venda_validada = VendaValidada(1, "Notebook Gamer", 5000.00, 2, date(2024, 3, 18), "cliente@example.com")
print(venda_validada)

try:
    venda_invalidada = VendaValidada(1, "Notebook Gamer", -5000.00, 2, date(2024, 3, 18), "cliente")
    print(venda_invalidada)
except Exception as e:
    print(e)
