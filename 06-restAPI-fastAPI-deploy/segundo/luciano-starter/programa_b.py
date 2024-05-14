import time

def dobra_o_numero(numero: int):
    return numero * 2

def le_o_ultimo_numero_do_arquivo():
    with open("recursos/arquivo.txt", "r") as file:
        ultimo_numero = int(file.readlines()[-1])
        return ultimo_numero

if __name__ == "__main__":
    while True: 
        ultimo_numero = le_o_ultimo_numero_do_arquivo()
        print(ultimo_numero)
        numero_dobrado = dobra_o_numero(ultimo_numero)
        print(numero_dobrado)
        time.sleep(1)