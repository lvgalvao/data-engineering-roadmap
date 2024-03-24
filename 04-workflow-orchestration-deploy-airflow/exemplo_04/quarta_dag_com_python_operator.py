from datetime import datetime

from airflow.decorators import dag, task
from airflow.models.baseoperator import cross_downstream

from time import sleep

@dag(start_date=datetime(2024, 3, 23), 
     schedule="@daily", 
     catchup=False)
def quarta_dag_com_python_operator():
    """
    minha primeira Pipipeline
    """
    @task
    def primeira_atividade():
        print("Primeira atividade iniciada")
        sleep(1)
        print("Primeira atividade finalizada")

    @task
    def segunda_atividade():
        print("Segunda atividade iniciada")
        sleep(1)
        print("Segunda atividade finalizada")

    @task
    def terceira_atividade():
        print("Terceira atividade iniciada")
        sleep(1)
        print("Terceira atividade finalizada")

    @task
    def quarta_atividade():
        print("Terceira atividade iniciada")
        sleep(1)
        print("Terceira atividade finalizada")

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()
    t4 = quarta_atividade()

    cross_downstream([t1,t2],[t3,t4])

quarta_dag_com_python_operator()