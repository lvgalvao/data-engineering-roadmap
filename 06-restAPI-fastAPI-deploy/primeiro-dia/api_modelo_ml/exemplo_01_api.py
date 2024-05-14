from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

modelo = joblib.load("modelo_casas.pkl")

class EspecificacoesCasa(BaseModel):
    tamanho: int
    quartos: int
    n_vagas: int

@app.post("/prever/")
def prever_preco(especificacoes_cada: EspecificacoesCasa):
    
    dados_entrada = [[especificacoes_cada.tamanho, especificacoes_cada.quartos, especificacoes_cada.n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    return {
        "preco_estimado": round(preco_estimado,2)
    }