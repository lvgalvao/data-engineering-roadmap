import random
import time

def numero_aleatorio():
    num = random.randint(1,95)
    print(num)
    with open("recursos/arquivo.txt", "a") as file:
        file.write(f"{num}\n")


if __name__ == "__main__":
    while True:
        numero_aleatorio()
        time.sleep(1)