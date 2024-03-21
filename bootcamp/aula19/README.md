# Aula 19: Fazendo nossa API

## O que é FastAPI?

FastAPI é uma estrutura (framework) web de alto desempenho para construir APIs com Python 3.6+ baseada em tipos de dados declarativos (graças ao Pydantic) e no padrão ASGI (Asynchronous Server Gateway Interface). Ele é projetado para ser fácil de usar, rápido para aprender e altamente eficiente em termos de desempenho, oferecendo suporte nativo a tipos de dados Python, tipagem de dados, validação automática de entrada e documentação interativa automática (gerada automaticamente pelo Swagger UI e ReDoc).

Principais características:

1. **Rápido**: Utiliza Python assíncrono e técnicas de otimização para alto desempenho.
2. **Fácil de usar**: Possui uma sintaxe declarativa e intuitiva, permitindo uma rápida prototipação.
3. **Tipagem de dados**: Utiliza a tipagem de dados Python para garantir a segurança e a consistência dos dados.
4. **Documentação automática**: Gera automaticamente documentação interativa para sua API.
5. **Suporte a OpenAPI e Swagger**: Total compatibilidade com esses padrões, permitindo integração com outras ferramentas.

## Exemplos de uso do FastAPI:

### 1. Criando uma API básica:

```python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

### 2. Definindo modelos de dados com Pydantic:

```python
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```

### Desafio

Criar nosso primeiro CRUD

1. **`POST /items/`: Cria um novo item**
    
    Esta rota permite criar um novo item no banco de dados. O cliente envia os dados do novo item no corpo da solicitação HTTP e o servidor adiciona esse item ao banco de dados. Aqui está como funciona:
    
    * **Verbo HTTP**: POST
    * **Endpoint**: `/items/`
    * **Ação**: Cria um novo item no banco de dados.
    * **Requisitos**: O corpo da solicitação deve conter os dados do novo item.
    * **Resposta**: Retorna o novo item criado.
2. **`GET /items/`: Retorna uma lista paginada de itens**
    
    Esta rota permite recuperar uma lista paginada de itens do banco de dados. O cliente pode especificar opcionalmente os parâmetros `skip` (quantos itens pular) e `limit` (quantos itens retornar) para paginação. Aqui está como funciona:
    
    * **Verbo HTTP**: GET
    * **Endpoint**: `/items/`
    * **Ação**: Retorna uma lista paginada de itens do banco de dados.
    * **Parâmetros de consulta**: `skip` (opcional, padrão = 0) e `limit` (opcional, padrão = 10).
    * **Resposta**: Retorna uma lista de itens conforme especificado pelos parâmetros de consulta.
3. **`GET /items/{item_id}`: Retorna um item específico com base no ID**
    
    Esta rota permite recuperar um item específico do banco de dados com base no ID fornecido. Aqui está como funciona:
    
    * **Verbo HTTP**: GET
    * **Endpoint**: `/items/{item_id}`
    * **Ação**: Retorna um item específico com base no ID fornecido.
    * **Parâmetros de caminho**: `item_id` (ID do item a ser recuperado).
    * **Resposta**: Retorna o item correspondente ao ID fornecido.
4. **`PUT /items/{item_id}`: Atualiza um item existente com base no ID**
    
    Esta rota permite atualizar os dados de um item existente no banco de dados com base no ID fornecido. O cliente envia os novos dados do item no corpo da solicitação HTTP. Aqui está como funciona:
    
    * **Verbo HTTP**: PUT
    * **Endpoint**: `/items/{item_id}`
    * **Ação**: Atualiza um item existente com base no ID fornecido.
    * **Parâmetros de caminho**: `item_id` (ID do item a ser atualizado).
    * **Requisitos**: O corpo da solicitação deve conter os novos dados do item.
    * **Resposta**: Retorna o item atualizado.
5. **`DELETE /items/{item_id}`: Exclui um item existente com base no ID**
    
    Esta rota permite excluir um item existente no banco de dados com base no ID fornecido. Aqui está como funciona:
    
    * **Verbo HTTP**: DELETE
    * **Endpoint**: `/items/{item_id}`
    * **Ação**: Exclui um item existente com base no ID fornecido.
    * **Parâmetros de caminho**: `item_id` (ID do item a ser excluído).
    * **Resposta**: Retorna o item excluído.

Essas operações fornecem uma API completa para gerenciar itens no banco de dados, permitindo criar, recuperar, atualizar e excluir itens de forma eficiente e segura. Certifique-se de que as operações estejam de acordo com os requisitos do seu projeto e que você implemente a lógica necessária para garantir a consistência e a segurança dos dados.