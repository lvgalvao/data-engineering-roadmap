from time import sleep

def primeira_atividade():
    print("Primeira atividade iniciada")
    sleep(1)
    print("Primeira atividade finalizada")

def segunda_atividade():
    print("Segunda atividade iniciada")
    sleep(1)
    print("Segunda atividade finalizada")

def terceira_atividade():
    print("Terceira atividade iniciada")
    sleep(1)
    print("Terceira atividade finalizada")

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline finalizada")

if __name__ == "__main__":
    pipeline()