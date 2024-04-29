import random
import time
from programa_04_decorador_exemplo import alou_decorator


@alou_decorator
def gerar_numero_aleatorio():
    num = random.randint(1, 10)
    print(num)
    with open('numeros.txt', 'a') as file:
        file.write(f"{num}\n")

if __name__ == "__main__":
    while True:
        gerar_numero_aleatorio()
        time.sleep(1)
