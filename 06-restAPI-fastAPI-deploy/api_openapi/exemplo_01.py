import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# URL da API
url = "https://api.openai.com/v1/images/generations"


# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"  # Substitua $OPENAI_API_KEY pelo seu token real
}

# Dados a serem enviados como corpo da requisição
body = {
    "model": "dall-e-3",
    "prompt": "a white siamese cat",
    "n": 1,
    "size": "1024x1024"
}

# Realizando a requisição POST
response = requests.post(
    url, 
    headers=headers, 
    data=json.dumps(body))

print(response.status_code)
print(response.json())