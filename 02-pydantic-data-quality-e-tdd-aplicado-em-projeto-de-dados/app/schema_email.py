import pandera as pa
from pandera.typing import Series

email_regex = r"[^@]+@[^@]+\.[^@]+"

class ProdutoSchemaEmail(pa.SchemaModel):
    id_produto: Series[int] = pa.Field(ge=1, le=10)
    nome: Series[str]
    quantidade: Series[int] = pa.Field(ge=20, le=200)
    preco: Series[float] = pa.Field(ge=5.0, le=120.0)
    categoria: Series[str]
    email: Series[str] = pa.Field(regex=email_regex)

    class Config:
        coerce = True
        strict = True