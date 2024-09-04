from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from dotenv import load_dotenv
from pydantic import BaseModel, ValidationError, Field
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

# Modelo Pydantic para o Parsing da Resposta
class QuoteModel(BaseModel):
    price: float
    volume_24h: float = Field(alias='volume_24h')
    market_cap: float = Field(alias='market_cap')
    last_updated: str = Field(alias='last_updated')

class BitcoinDataModel(BaseModel):
    symbol: str
    quote: dict

    def get_usd_quote(self) -> QuoteModel:
        return QuoteModel(**self.quote['USD'])

class ApiResponseModel(BaseModel):
    data: dict
    status: dict

    def get_bitcoin_data(self) -> BitcoinDataModel:
        return BitcoinDataModel(**self.data['BTC'])

# Função que faz a requisição à API e processa os dados usando Pydantic
def consultar_cotacao_bitcoin():
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        
        # Parsing da resposta usando Pydantic
        api_response = ApiResponseModel(**data)
        bitcoin_data = api_response.get_bitcoin_data()
        quote = bitcoin_data.get_usd_quote()

        # Imprimir os dados da cotação
        print(f"Última cotação do Bitcoin: ${quote.price:.2f} USD")
        print(f"Volume 24h: ${quote.volume_24h:.2f} USD")
        print(f"Market Cap: ${quote.market_cap:.2f} USD")
        print(f"Última atualização: {quote.last_updated}")

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(f"Erro na requisição: {e}")
    except ValidationError as e:
        print(f"Erro ao validar a resposta da API: {e}")

# Executa a função para consultar a cotação do Bitcoin
consultar_cotacao_bitcoin()
