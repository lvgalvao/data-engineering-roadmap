from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    idade: int
    email: str

class VendasSchema(BaseModel):
    produto: str
    quantidade: int
    preco: float

class RecursosHumanosSchema(BaseModel):
    funcionario: str
    departamento: str
    salario: float
