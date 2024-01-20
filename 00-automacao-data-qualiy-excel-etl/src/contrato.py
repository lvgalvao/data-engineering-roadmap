from pydantic import BaseModel, EmailStr

class UsuarioSchema(BaseModel):
    nome: str
    idade: int
    email: str

class VendasSchema(BaseModel):
    produto: str
    quantidade: int
    preco: float
    email: EmailStr

class RecursosHumanosSchema(BaseModel):
    funcionario: str
    departamento: str
    salario: float
