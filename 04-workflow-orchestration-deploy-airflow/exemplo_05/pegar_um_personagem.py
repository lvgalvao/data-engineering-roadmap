import requests

API = "https://www.boredapi.com/api/activity"

def descobrir_atividade():

    def pegar_atividade():
        r = requests.get(API, timeout=10)
        return r.json()
    
    def salvar_atividade_em_um_arquivo(response):
        filepath = "./activity.txt"	
        with open(filepath, "w") as f:
            f.write(f"Hoje eu vou: {response['activity']}")
        return filepath

    def ler_atividade_do_arquivo(filepath):
        with open(filepath, "r") as f:
            print(f.read())

    real_response = pegar_atividade()
    real_caminho = salvar_atividade_em_um_arquivo(real_response)
    ler_atividade_do_arquivo(real_caminho)

descobrir_atividade()
