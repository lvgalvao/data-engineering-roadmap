from confluent_kafka import Consumer, KafkaError
from dotenv import load_dotenv
import os
import csv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do consumidor
conf = {
    'bootstrap.servers': os.getenv('BOOTSTRAP_SERVERS'),
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': os.getenv('SASL_USERNAME'),
    'sasl.password': os.getenv('SASL_PASSWORD'),
    'group.id': 'outro-python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Criação do consumidor
consumer = Consumer(**conf)

# Inscrição no tópico
topic = os.getenv('TOPIC_PRODUCER')
consumer.subscribe([topic])

# Função para processar mensagens
def consume_messages():
    # Nome do arquivo CSV
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório do script atual
    csv_file = os.path.join(script_dir, 'messages_02.csv')  # Caminho completo para o arquivo CSV
    
    # Abrir o arquivo CSV em modo de escrita
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Key', 'Value'])  # Escrever cabeçalho no CSV
        
        try:
            while True:
                msg = consumer.poll(1.0)  # Espera até 1 segundo por uma nova mensagem
                # Exibe a mensagem recebida
                if msg is None:  # Se nenhuma mensagem foi recebida
                    continue
                if msg.error():  # Se houve um erro ao receber a mensagem
                    continue
                key = msg.key().decode('utf-8')
                value = msg.value().decode('utf-8')
                print(f"Received message: Key: {key}, Value: {value}")
                # Escreve a mensagem no CSV
                writer.writerow([key, value])
        except KeyboardInterrupt:
            pass
        finally:
            print("Closing consumer.")
            consumer.close()

if __name__ == "__main__":
    consume_messages()
