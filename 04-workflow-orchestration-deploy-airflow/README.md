# Orquestração de ETLs

##  Overview

O Apache Airflow é uma plataforma projetada para criar, agendar e monitorar fluxos de trabalho de forma programática.

Quando os fluxos de trabalho são definidos como código, eles se tornam mais fáceis de manter, versionar, testar e colaborar.

Utilize o Airflow para compor fluxos de trabalho como grafos acíclicos dirigidos (DAGs) de tarefas. O agendador do Airflow executa suas tarefas em uma série de workers respeitando as dependências definidas. Ferramentas de linha de comando abrangentes facilitam a realização de operações complexas nos DAGs. A interface de usuário intuitiva permite visualizar facilmente os pipelines em execução, monitorar o progresso e resolver problemas quando necessário.

O Airflow é especialmente útil em contextos de engenharia de dados e ciência de dados, pois permite a automação e a orquestração de processos complexos de tratamento de dados, treinamento de modelos de machine learning, execução de ETLs e muito mais. Tudo isso contribui para uma gestão mais eficiente do ciclo de vida dos dados e dos modelos preditivos.

## User Interface

- **DAGs**: Visão deral do seu ambiente.

  ![DAGs](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/dags.png)

- **Grid**: Visão de todas as execuções de um DAG.

  ![Grid](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/grid.png)

- **Graph**: Visão de todas as tarefas de um DAG e suas dependências.

  ![Graph](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/graph.png)

- **Task Duration**: Tempo de execução de cada tarefa de um DAG.

  ![Task Duration](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/duration.png)

- **Gantt**: Duração de cada execução de um DAG.

  ![Gantt](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/gantt.png)

- **Code**: Código de cada DAG.

  ![Code](https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/img/code.png)

## Mas entre nós

Eu realmente preciso do Airflow?

Vamos pensar em uma pipeline inicial, onde possui 3 atividades e uma pipeline que encadeia ela.

![Exemplo_00](./pic/exemplo_00.png)

exemplo_00.py
```python
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
```

Qual o problema de realizar uma ETL desse jeito?

![Exemplo_01](./pic/exemplo_01.png)

Como programar ela a cada 10 segundos?

exemplo_01.py
```python
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
    while True:
        pipeline()
        sleep(10)
```

Qual o problema de realizar uma ETL desse jeito?

![Exemplo_02](./pic/exemplo_02.png)

Como ter o log a auditoria do que foi feito?

```python
from time import sleep

from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")

def primeira_atividade():
    logger.info("Primeira atividade iniciada")
    sleep(1)
    logger.info("Primeira atividade finalizada")

def segunda_atividade():
    logger.info("Segunda atividade iniciada")
    sleep(1)
    logger.info("Segunda atividade finalizada")

def terceira_atividade():
    logger.info("Terceira atividade iniciada")
    sleep(1)
    logger.info("Terceira atividade finalizada")

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline finalizada")

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(10)
```

Qual o problema de realizar uma ETL desse jeito?

![Exemplo_02](./pic/exemplo_02.png)

Como ter o log a auditoria do que foi feito?

## Vocês entenderam onde eu quero chegar

Gastei 10% do tempo gerando valor e 90% do tempo reinventando a roda



- Eu realmente preciso do Airflow?
- A história do Apache Airflow.
- Por que você deve usar o Airflow.
- Quando você deve usar o Airflow.
- Conceitos centrais do Airflow.

### Começando

### Airflow principais conceitos

#### Básico

##### BashOperator

##### Connections

##### DAGs

##### Manage Airflow Code
