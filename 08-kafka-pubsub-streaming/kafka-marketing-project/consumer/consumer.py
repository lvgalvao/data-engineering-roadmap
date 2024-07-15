import time
import random
from confluent_kafka import Consumer, KafkaError
import json
import os
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Configuração do Consumer
consumer_conf = {
    'bootstrap.servers': os.environ['BOOTSTRAP_SERVERS'],
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': os.environ['SASL_USERNAME'],
    'sasl.password': os.environ['SASL_PASSWORD'],
    'group.id': 'temperature-consumer-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(consumer_conf)
consumer.subscribe(['marketing-project'])

# Configuração do PostgreSQL
db_url = "postgresql://postgres_kafka_user:UQ4PAxSQbukeWVcFEDpdNquS6zhbt8zs@dpg-cq8vi35ds78s7396a4og-a.oregon-postgres.render.com/postgres_kafka_sink"
engine = create_engine(db_url)

def consume_messages():
    batch_size = 100  # Número de mensagens para processar por batch
    batch_interval = 5  # Intervalo de tempo (em segundos) entre os batches
    messages = []
    start_time = time.time()  # Inicializa start_time dentro da função

    try:
        while True:
            msg = consumer.poll(1.0)  # Espera até 1 segundo por uma nova mensagem
            if msg is None:
                continue
            if msg.error():
                continue

            value = json.loads(msg.value().decode('utf-8'))  # Converte o valor para JSON
            # Desnormalizar a mensagem
            data = {
                'id': value['id'],
                'latitude': value['latitude'],
                'longitude': value['longitude'],
                'temperature': value['temperature'],
                'time': datetime.now()  # Captura o tempo atual da mensagem
            }
            messages.append(data)

            # Processar batch quando atingir o tamanho ou o intervalo de tempo
            if len(messages) >= batch_size or (time.time() - start_time) >= batch_interval:
                df = pd.DataFrame(messages)
                df.to_sql('temperature_data', engine, if_exists='append', index=False)
                messages = []  # Limpar lista de mensagens após salvar no banco
                start_time = time.time()  # Resetar o contador de tempo

    except KeyboardInterrupt:
        pass
    finally:
        print("Closing consumer.")
        consumer.close()

if __name__ == "__main__":
    start_time = time.time()
    consume_messages()
