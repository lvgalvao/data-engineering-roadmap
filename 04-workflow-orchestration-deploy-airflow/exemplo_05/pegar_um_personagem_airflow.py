from airflow.decorators import dag, task

from airflow.models import Variable

from datetime import datetime

import requests

API = "https://www.boredapi.com/api/activity"

@dag(dag_id="pegar_um_personagem_airflow",
     description="pipeline que pega um personagem, salva em um arquivo temp e le",
     schedule="* * * * *",
     start_date=datetime(2024,3,23),
     catchup=False,
     tags=["tutorial"])
def descobrir_atividade():

    @task
    def pegar_atividade():
        r = requests.get(API, timeout=10)
        return r.json()
    
    @task
    def salvar_atividade_em_um_arquivo(response):
        filepath = Variable.get("activity_file")
        with open(filepath, "a") as f:
            f.write(f"Hoje eu vou: {response['activity']}")
        return filepath

    @task
    def ler_atividade_do_arquivo(filepath):
        with open(filepath, "r") as f:
            print(f.read())

    t1 = pegar_atividade()
    t2 = salvar_atividade_em_um_arquivo(t1)
    t3 = ler_atividade_do_arquivo(t2)

    t1 >> t2 >> t3

descobrir_atividade()
