import time
import random
from confluent_kafka import Producer
import uuid
from faker import Faker
import json
import os

fake = Faker('pt_BR')

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Configuração do Producer
producer_conf = {
    'bootstrap.servers': os.environ['BOOTSTRAP_SERVERS'],
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': os.environ['SASL_USERNAME'],
    'sasl.password': os.environ['SASL_PASSWORD']
}

def generate_unique_id():
    return int(str(uuid.uuid4().int)[:8])

producer = Producer(producer_conf)

def generate_initial_data(id):
    lat = random.uniform(-33.0, 5.0)
    lon = random.uniform(-73.0, -34.0)
    address = fake.address()
    temperature_range = 'low' if random.random() < 0.95 else 'high'
    data = {
        'id': id,
        'latitude': lat,
        'longitude': lon,
        'address': address,
        'temperature_range': temperature_range
    }
    return data

def generate_temperature(temperature_range):
    if temperature_range == 'low':
        temperature = random.gauss(2.5, 1.0)
    else:
        temperature = random.uniform(20.0, 40.0)
    return round(temperature, 2)

if __name__ == '__main__':
    producer_id = generate_unique_id()
    initial_data = generate_initial_data(producer_id)
    while True:
        temperature = generate_temperature(initial_data['temperature_range'])
        data = initial_data.copy()
        data['temperature'] = temperature
        producer.produce('marketing-project', key=str(producer_id), value=json.dumps(data), callback=delivery_report)
        producer.poll(1)
        time.sleep(5)
