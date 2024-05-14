import random

def numero_aleatorio():
    num = random.randint(1,95)
    print(num)
    return num

def dobra_o_numero(numero: int):
    return numero * 2

def main():
    num = numero_aleatorio()
    return dobra_o_numero(num)

if __name__ == "__main__":
    numero_dobrado = main()
    print(numero_dobrado)