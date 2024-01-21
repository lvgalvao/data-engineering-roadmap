from pydantic import BaseModel, EmailStr

class UsuarioSchema(BaseModel):
    """
    Define o esquema para os dados do usuário.

    Attributes:
        nome (str): Nome do usuário.
        idade (int): Idade do usuário.
        email (str): Email do usuário.
    """
    nome: str
    idade: int
    email: str

class VendasSchema(BaseModel):
    """
    Define o esquema para os dados de vendas.

    Attributes:
        produto (str): Nome do produto.
        quantidade (int): Quantidade vendida.
        preco (float): Preço do produto.
        email (EmailStr): Email de contato para a venda.
    """
    produto: str
    quantidade: int
    preco: float
    email: EmailStr

class RecursosHumanosSchema(BaseModel):
    """
    Define o esquema para os dados de recursos humanos.

    Attributes:
        funcionario (str): Nome do funcionário.
        departamento (str): Departamento do funcionário.
        salario (float): Salário do funcionário.
    """
    funcionario: str
    departamento: str
    salario: float

