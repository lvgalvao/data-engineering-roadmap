import random
import time

def numero_aleatorio():
    """ Gera um numero aleatorio. """
    return random.randint(1, 10)

def dobra_um_numero(num):
    """ Calcula o quadrado do dobro de um número. """
    return num ** 2

if __name__ == "__main__":
    while True:
        num = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
        resultado = dobra_um_numero(num)
        print(f"O quadrado do dobro de {num} é {resultado}")
        time.sleep(1)  # Pausa a execução por 1 segundo
