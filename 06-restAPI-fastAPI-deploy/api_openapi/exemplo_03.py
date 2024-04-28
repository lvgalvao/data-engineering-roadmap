import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração inicial da chave da API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# URL da API
url = "https://api.openai.com/v1/images/generations"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# Interface do Streamlit
st.title('Gerador de Imagens')
prompt = st.text_area('Digite o prompt para gerar uma imagem:', value='Descrição da imagem aqui')

if st.button('Gerar Imagem'):
    # Corpo da requisição
    body = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    # Realiza a requisição POST
    response = requests.post(url, headers=headers, data=json.dumps(body))

    if response.status_code == 200:
        # Extrai a URL da imagem
        url_image = response.json()["data"][0]["url"]
        # Exibe a imagem na interface do Streamlit
        st.image(url_image)
    else:
        st.error("Erro ao gerar a imagem. Por favor, tente novamente.")
