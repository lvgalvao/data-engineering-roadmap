from dataclasses import dataclass

@dataclass
class VendaDataClass:
    id: int
    produto: str
    valor: float
    quantidade: int
    data: str
    email_comprador: str

# Exemplo de uso
venda_dc = VendaDataClass(1, "Notebook Gamer", 5000.00, 2, "2024-03-18", "cliente@example.com")
print(venda_dc)

