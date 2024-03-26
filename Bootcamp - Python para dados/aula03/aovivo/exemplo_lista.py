from typing import Dict, Optional, Any

import json

lista: Any = ["Sapato", 39, 10.38, True]

produto_01: Dict[str, Any] = {
    "nome":"Sapato",
    "quantidade":39,
    "preco": 10.38,
    "diponibilidade": True
}

produto_02: dict = {
    "nome":"Televisao",
    "quantidade":10,
    "preco": 70.38,
    "diponibilidade": "false"
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)
