from fastapi import FastAPI
import joblib
from pydantic import BaseModel, EmailStr, PositiveInt, PositiveFloat
from typing import Optional

app = FastAPI()

modelo = joblib.load("modelo_casas.pkl")

class EspecificacoesCasa(BaseModel):
    tamanho: PositiveInt
    quartos: PositiveInt
    n_vagas: PositiveInt

class EspecificacoesCasaRequest(EspecificacoesCasa):
    email: Optional[EmailStr] = None

class EspecificacoesCasaResponse(BaseModel):
    preco_estimado: PositiveFloat
    dados: EspecificacoesCasa

@app.post("/prever/", response_model=EspecificacoesCasaResponse)
def prever_preco(especificacoes_cada: EspecificacoesCasa):
    
    dados_entrada = [[especificacoes_cada.tamanho, especificacoes_cada.quartos, especificacoes_cada.n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    return EspecificacoesCasaResponse(preco_estimado=preco_estimado, dados=especificacoes_cada)