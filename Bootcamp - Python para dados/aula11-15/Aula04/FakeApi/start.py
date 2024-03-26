from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random


app = FastAPI(debug=True)
fake = Faker()

file_name = 'data/products.csv'
df = pd.read_csv(file_name)
df['indice'] = range(1, len(df) +1)
df.set_index('indice', inplace=True)

lojapadraoonline = 11

@app.get("/")
async def hello_world():
    return 'Coca-Cola me patrocina!'

@app.get("/gerar_compra")
async def gerar_compra():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]
    return [{
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["Product Name"],
            "ean": int(tuple["EAN"]),
            "price":  round(float(tuple["Price"])*1.2,2),
            "clientPosition": fake.location_on_land(),
            "store": lojapadraoonline,
            "dateTime": fake.iso8601()
        }]

@app.get("/gerar_compras/{numero_registro}")
async def gerar_compra(numero_registro: int):
    
    if numero_registro < 1:
        return {"error" : "O número deve ser maior que 1"}
 
    respostas = []
    for _ in range(numero_registro):
        try:
            index = random.randint(1, len(df)-1)
            tuple = df.iloc[index]
            compra = {
                    "client": fake.name(),
                    "creditcard": fake.credit_card_provider(),
                    "product": tuple["Product Name"],
                    "ean": int(tuple["EAN"]),
                    "price":  round(float(tuple["Price"])*1.2,2),
                    "clientPosition": fake.location_on_land(),
                    "store": lojapadraoonline,
                    "dateTime": fake.iso8601()
                    }
            respostas.append(compra)
        except IndexError as e:
            print(f"Erro de índice: {e}")
        except ValueError as e:
            print(f"Erro inesperado: {e}")
            compra = {
                    "client": fake.name(),
                    "creditcard": fake.credit_card_provider(),
                    "product": "error",
                    "ean": 0,
                    "price":  0.0,
                    "clientPosition": fake.location_on_land(),
                    "store": lojapadraoonline,
                    "dateTime": fake.iso8601()
                    }
            respostas.append(compra)
        except Exception as e:
            print(f"Erro inesperado: {e}")
    return respostas