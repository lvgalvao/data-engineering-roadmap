import urllib3
import json
import os

# Carregar variáveis de ambiente
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
api_key = ''  # Chave da API obtida das variáveis de ambiente

# Parâmetros da requisição para obter a cotação do Bitcoin
parameters = {
 'symbol': 'BTC',  # Identificando o Bitcoin pelo símbolo
 'convert': 'USD'  # Convertendo a cotação para USD
}

# Headers com a chave da API
headers = {
 'Accept': 'application/json',
 'X-CMC_PRO_API_KEY': api_key  # Obtendo a chave da API das variáveis de ambiente
}

# Criar um PoolManager para gerenciar conexões
http = urllib3.PoolManager()

# Função Lambda
def lambda_handler(event, context):
 try:
     # Converte os parâmetros para o formato de query string
     query_string = '&'.join([f'{key}={value}' for key, value in parameters.items()])
     full_url = f"{url}?{query_string}"
     
     # Fazendo o request GET para a API
     response = http.request('GET', full_url, headers=headers)
     data = json.loads(response.data.decode('utf-8'))
     
     # Verificar se os dados do Bitcoin estão presentes na resposta
     if 'data' in data and 'BTC' in data['data']:
         bitcoin_data = data['data']['BTC']
         usd_quote = bitcoin_data['quote']['USD']
         
         # Log da resposta
         print(f"Cotação do Bitcoin obtida: {usd_quote}")
     else:
         print("Erro ao obter a cotação do Bitcoin:", data.get('status', {}).get('error_message', 'Erro desconhecido'))

 except urllib3.exceptions.HTTPError as e:
     print(f"Erro na requisição: {e}")
