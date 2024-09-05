from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import schedule
import json
import os
import time
import psycopg2
from psycopg2 import sql

# Carregar variáveis do arquivo .env
load_dotenv()

# URL da API de Produção para obter a última cotação do Bitcoin
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Parâmetros da requisição para obter a cotação do Bitcoin
parameters = {
    'symbol': 'BTC',  # Identificando o Bitcoin pelo símbolo
    'convert': 'USD'  # Convertendo a cotação para USD
}

# Headers com a chave da API obtida do arquivo .env
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv('CMC_API_KEY'),  # Obtendo a chave do .env
}

# Criar uma sessão
session = Session()
session.headers.update(headers)

# Configuração do banco de dados RDS
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para criar a tabela caso ainda não exista
def criar_tabela():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        
        # Criação da tabela
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS bitcoin_quotes (
            id SERIAL PRIMARY KEY,
            price NUMERIC,
            volume_24h NUMERIC,
            market_cap NUMERIC,
            last_updated TIMESTAMP
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabela criada ou já existente.")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")

# Função para salvar os dados no banco de dados
def salvar_no_rds(usd_quote):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        
        # Inserção dos dados na tabela
        insert_query = sql.SQL(
            "INSERT INTO bitcoin_quotes (price, volume_24h, market_cap, last_updated) VALUES (%s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            usd_quote['price'],
            usd_quote['volume_24h'],
            usd_quote['market_cap'],
            usd_quote['last_updated']
        ))
        conn.commit()
        cursor.close()
        conn.close()
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados no RDS: {e}")

# Função que faz a requisição à API e salva a última cotação do Bitcoin
def consultar_cotacao_bitcoin():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        # Verificar se os dados do Bitcoin estão presentes na resposta
        if 'data' in data and 'BTC' in data['data']:
            bitcoin_data = data['data']['BTC']
            usd_quote = bitcoin_data['quote']['USD']
            
            # Salvar os dados no banco de dados
            salvar_no_rds(usd_quote)
        else:
            print("Erro ao obter a cotação do Bitcoin:", data['status'].get('error_message', 'Erro desconhecido'))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição: {e}")

# Criar a tabela no banco de dados
criar_tabela()

# Agendar a função para rodar a cada 15 segundos
schedule.every(15).seconds.do(consultar_cotacao_bitcoin)

# Loop principal para manter o agendamento ativo
if __name__ == "__main__":
    print("Iniciando o agendamento para consultar a API a cada 15 segundos...")
    while True:
        schedule.run_pending()
        time.sleep(1)
