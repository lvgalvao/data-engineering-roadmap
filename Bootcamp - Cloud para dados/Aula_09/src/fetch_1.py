from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
import json
import os

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

# Função que faz a requisição à API e imprime a última cotação do Bitcoin
def consultar_cotacao_bitcoin():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        # Verificar se os dados do Bitcoin estão presentes na resposta
        if 'data' in data and 'BTC' in data['data']:
            bitcoin_data = data['data']['BTC']
            usd_quote = bitcoin_data['quote']['USD']
            
            # Imprimir os dados da cotação
            print(f"Última cotação do Bitcoin: ${usd_quote['price']:.2f} USD")
            print(f"Volume 24h: ${usd_quote['volume_24h']:.2f} USD")
            print(f"Market Cap: ${usd_quote['market_cap']:.2f} USD")
            print(f"Última atualização: {usd_quote['last_updated']}")
        else:
            print("Erro ao obter a cotação do Bitcoin:", data['status'].get('error_message', 'Erro desconhecido'))

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição: {e}")

# Executa a função para consultar a cotação do Bitcoin
consultar_cotacao_bitcoin()
