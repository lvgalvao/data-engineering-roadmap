from pymongo import MongoClient
from fastapi import FastAPI
import joblib
from pydantic import BaseModel, EmailStr, PositiveInt, PositiveFloat
from typing import Optional, List

app = FastAPI()

modelo = joblib.load("./src/modelo_casas.pkl")

class EspecificacoesCasa(BaseModel):
    tamanho: PositiveInt
    quartos: PositiveInt
    n_vagas: PositiveInt

class EspecificacoesCasaRequest(EspecificacoesCasa):
    email: EmailStr = None

class EspecificacoesCasaResponse(BaseModel):
    preco_estimado: PositiveFloat
    dados: EspecificacoesCasaRequest

# Configuração do MongoDB
client = MongoClient('mongodb://root:example@mongodb:27017')
db = client['dbmongo']
collection = db['dbscrm']

@app.post("/quanto-cobrar-de-casa/", response_model=EspecificacoesCasaResponse)
def prever_preco(especificacoes_cada: EspecificacoesCasaRequest):
    
    dados_entrada = [[especificacoes_cada.tamanho, especificacoes_cada.quartos, especificacoes_cada.n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    response = EspecificacoesCasaResponse(preco_estimado=preco_estimado, dados=especificacoes_cada)
    collection.insert_one(response.model_dump())
    return response

@app.get("/mkt/", response_model=List[EspecificacoesCasaResponse])
def read_all_leads():
    casas = list(collection.find({}))
    return [EspecificacoesCasaResponse(preco_estimado=casa['preco_estimado'], dados=casa['dados']) for casa in casas]