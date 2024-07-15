# https://kafka-python.readthedocs.io/en/master/#kafkaproducer
import json
import os
import random
import time
import uuid

from faker import Faker
from kafka import KafkaProducer

fake = Faker()

TOPIC = os.environ.get('TOPIC', 'foobar')
BOOTSTRAP_SERVERS = os.environ.get(
    'BOOTSTRAP_SERVERS', 'localhost:9091,localhost:9092,localhost:9093'
).split(',')


def criar_transacao(contador):
    mensagem = {
        'id_sequencia': contador,
        'id_usuario': str(fake.random_int(min=20000, max=100000)),
        'id_transacao': str(uuid.uuid4()),
        'id_produto': str(uuid.uuid4().fields[-1])[:5],
        'endereco': str(
            fake.street_address()
            + ' | '
            + fake.city()
            + ' | '
            + fake.country_code()
        ),
        'cadastro_em': str(fake.date_time_this_month()),
        'id_plataforma': str(random.choice(['Mobile', 'Laptop', 'Tablet'])),
        'mensagem': 'transacao feita pelo usuario {}'.format(
            str(uuid.uuid4().fields[-1])
        ),
    }
    return mensagem


def configurar_produtor():
    try:
        produtor = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        )
        return produtor
    except Exception as e:
        if e == 'NoBrokersAvailable':
            print('aguardando os brokers ficarem disponíveis')
        return 'nao-disponivel'


print('configurando produtor, verificando se os brokers estão disponíveis')
produtor = 'nao-disponivel'

while produtor == 'nao-disponivel':
    print('brokers ainda não disponíveis')
    time.sleep(5)
    produtor = configurar_produtor()

print('brokers estão disponíveis e prontos para produzir mensagens')
contador = 0

while True:
    contador += 1
    mensagem_json = criar_transacao(contador)
    produtor.send(TOPIC, mensagem_json)
    print(
        'mensagem enviada para o kafka com id de sequência {}'.format(contador)
    )
    time.sleep(2)

produtor.close()
