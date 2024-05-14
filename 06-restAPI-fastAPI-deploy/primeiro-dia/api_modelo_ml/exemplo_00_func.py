import joblib

modelo = joblib.load("modelo_casas.pkl")

def prever_preco(tamanho: int,
                 quartos: int,
                 n_vagas: int):
    
    dados_entrada = [[tamanho, quartos, n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    return round(preco_estimado,2)

print(prever_preco(200,3,3))