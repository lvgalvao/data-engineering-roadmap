import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração inicial da chave da API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# URL da API para completar texto
url = "https://api.openai.com/v1/completions"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# Interface do Streamlit
st.title('Conversor de SQL: SQL Server para PostgreSQL')
query_sql_server = st.text_area('Digite a consulta SQL Server aqui:')
print(query_sql_server)

if st.button('Converter para PostgreSQL'):
    # Prompt de conversão
    prompt = f"Convert this SQL Server query to a PostgreSQL query: {query_sql_server}"
    
    # Corpo da requisição
    body = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 1000
    }

    # Realiza a requisição POST
    response = requests.post(url, headers=headers, data=json.dumps(body))

    if response.status_code == 200:
        # Extrai a resposta e apresenta a consulta convertida
        postgres_query = response.json()["choices"][0]["text"].strip()
        st.text_area('Consulta PostgreSQL:', value=postgres_query, height=700)
    else:
        st.error("Erro na conversão. Por favor, tente novamente.")
