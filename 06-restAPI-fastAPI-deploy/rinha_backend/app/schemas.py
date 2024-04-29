from enum import Enum
from typing import Optional

from pydantic import BaseModel,Field

class TransactionTypeEnum(str, Enum):
    credito = 'c'
    debito = 'd'

class TransactionBase(BaseModel):
    valor: int
    tipo: TransactionTypeEnum
    descricao: str = Field(max_length=10, min_length=1)

class TransactionCreateRequest(TransactionBase):
    pass

class ClienteBase(BaseModel):
    limite: int
    saldo: int

class ClienteResponse(ClienteBase):
    pass

class ClientRequest(ClienteBase):
    pass

class ClientCreateRequest(ClienteBase):
    id: int

class ClienteUpdateRequest(BaseModel):
    saldo: Optional[float] = None
    limite: Optional[float] = None
