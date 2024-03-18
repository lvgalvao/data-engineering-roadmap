from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, PositiveInt, validate_call


class NumeroPositivo(BaseModel):
    numero: PositiveInt

@validate_call()
def calculadora(x: NumeroPositivo, y: NumeroPositivo) -> NumeroPositivo:
    return x + y

print(calculadora(4,-5))
print(calculadora(6,7))