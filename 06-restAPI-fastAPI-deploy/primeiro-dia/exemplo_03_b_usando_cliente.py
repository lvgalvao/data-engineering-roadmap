import time
import requests

def dobrar_numero(num):
    return num * 2

def ler_ultimo_numero():
    url = "http://127.0.0.1:8000/gerar_numero_aleatorio"
    response = requests.get(url)
    data = response.json() # response.test
    return data["data"] # data


if __name__ == "__main__":
    while True:
        num = ler_ultimo_numero()
        if num is not None:
            resultado = dobrar_numero(num)
            print(f"O quadrado do dobro do último número {num} é {resultado}")
            time.sleep(1)