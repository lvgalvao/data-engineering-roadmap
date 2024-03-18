from dataclasses import dataclass
import re
from datetime import date

def validar_valor(valor: float) -> float:
    if valor <= 0:
        raise ValueError("Valor deve ser um float positivo.")
    return valor

def validar_quantidade(quantidade: int) -> int:
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser um int positivo.")
    return quantidade

def validar_email(email: str) -> str:
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("E-mail do comprador inválido.")
    return email

@dataclass
class VendaValidada:
    id: int
    produto: str
    valor: float
    quantidade: int
    data: date
    email_comprador: str

    def __post_init__(self):
        self.valor = validar_valor(self.valor)
        self.quantidade = validar_quantidade(self.quantidade)
        self.email_comprador = validar_email(self.email_comprador)

# Exemplo de uso com try-except
try:
    venda_validada = VendaValidada(id=1, produto="Notebook Gamer", valor=5000.00, quantidade=2, data=date(2024, 3, 18), email_comprador="cliente@example.com")
    print(venda_validada)
except ValueError as e:
    print(e)

try:
    venda_invalida = VendaValidada(id=2, produto="Mouse Sem Fio", valor=-30.00, quantidade=3, data=date(2024, 3, 19), email_comprador="clienteinvali.do")
    print(venda_invalida)
except ValueError as e:
    print(e)
