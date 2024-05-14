import streamlit as st
import requests

# Função para enviar dados para a API e receber a previsão
def get_previsao(tamanho, quartos, n_vagas, email):
    url = 'http://backend:8000/quanto-cobrar-de-casa/'  # Endereço da API FastAPI
    data = {
        "tamanho": tamanho,
        "quartos": quartos,
        "n_vagas": n_vagas,
        "email": email if email else None  # Inclui o email na requisição apenas se for fornecido
    }
    response = requests.post(url, json=data)
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)  # Print or log the raw response
    try:
        return response.json()  # Attempt to parse JSON
    except ValueError:
        # Handle the case where parsing JSON fails
        print("Failed to decode JSON from response:")
        print(response.text)
        return None

# Interface do usuário no Streamlit
st.title('Quanto vale o seu imóvel')

# Entrada de dados pelo usuário
tamanho = st.number_input('Insira o tamanho da casa (em m²):', min_value=10.0, step=0.1, format="%.1f")
quartos = st.number_input('Insira o número de quartos:', min_value=1, step=1)
n_vagas = st.number_input('Insira o número de vagas de garagem:', min_value=0, max_value=4, step=1)
email = st.text_input('Insira seu email (opcional):', '')

# Botão para fazer a previsão
if st.button('Prever preço'):
    resposta = get_previsao(tamanho, quartos, n_vagas, email)
    if 'preco_estimado' in resposta:
        st.success(f'O preço estimado da casa é: R${resposta["preco_estimado"]:.2f}')
    else:
        st.error('Erro ao obter previsão.')
