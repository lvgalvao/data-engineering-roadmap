from pydantic import BaseModel, EmailStr, ValidationError, PositiveInt, PositiveFloat
from datetime import date

class VendaPydantic(BaseModel):
    id: int
    produto: str
    valor: PositiveFloat
    quantidade: PositiveInt
    data: date
    email_comprador: EmailStr

# Exemplo de uso
try:
    venda_pydantic = VendaPydantic(id=1, produto="Notebook Gamer", valor=5000.00, quantidade=2, data=date(2024, 3, 18), email_comprador="cliente@example.com")
    print(venda_pydantic)
except ValidationError as e:
    print(e.json())

# Exemplo de uso
try:
    venda_pydantic = VendaPydantic(id=1, produto="Notebook Gamer", valor=-5000.00, quantidade=2, data=date(2024, 3, 18), email_comprador="cliente@example.com")
    print(venda_pydantic)
except ValidationError as e:
    print(e)

