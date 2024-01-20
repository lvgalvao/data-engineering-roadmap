from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    idade: int
    email: str