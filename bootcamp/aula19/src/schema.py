from pydantic import BaseModel
from typing import Union

class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int