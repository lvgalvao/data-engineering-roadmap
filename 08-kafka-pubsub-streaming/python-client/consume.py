# https://kafka-python.readthedocs.io/en/master/#kafkaproducer
import json
import os
import time
from datetime import datetime

from kafka import KafkaConsumer

TOPIC = os.environ.get('TOPIC', 'foobar')
CONSUMER_GROUP = os.environ.get('CONSUMER_GROUP', 'cg-group-id')
BOOTSTRAP_SERVERS = os.environ.get(
    'BOOTSTRAP_SERVERS', 'localhost:9091,localhost:9092,localhost:9093'
).split(',')

print('iniciando')


def configurar_consumidor():
    try:
        consumidor = KafkaConsumer(
            TOPIC,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            auto_offset_reset='latest',
            enable_auto_commit=True,
            group_id=CONSUMER_GROUP,
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        )
        return consumidor

    except Exception as e:
        if e == 'NoBrokersAvailable':
            print('aguardando os brokers ficarem disponíveis')
        return 'nao-disponivel'


def diferenca_tempo(received_time):
    agora = datetime.now().strftime('%s')
    return int(agora) - received_time


print('iniciando consumidor, verificando se os brokers estão disponíveis')
consumidor = 'nao-disponivel'

while consumidor == 'nao-disponivel':
    print('brokers ainda não disponíveis')
    time.sleep(5)
    consumidor = configurar_consumidor()

print('brokers estão disponíveis e prontos para consumir mensagens')

for mensagem in consumidor:
    try:
        print(mensagem.value)
        # print(f"Mensagem recebida em: {mensagem.timestamp}")
        # agora = datetime.now().strftime("%s")
        # print(f"Timestamp atual {agora}")
    except Exception as e:
        print('ocorreu uma exceção no consumo')
        print(e)

# Fechar o consumidor
print('fechando consumidor')
consumidor.close()
