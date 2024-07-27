import io
from datetime import datetime

import numpy as np
import pandas as pd
import streamlit as st

# 1. Títulos e Texto
titulo = "Aula Introdutória ao Streamlit"
cabecalho = "Aprendendo os Principais Métodos"

# Exibição de Texto
subcabecalho_texto = "Métodos de Exibição de Texto"

# Texto simples
texto_simples = (
    "Streamlit facilita a criação de aplicações web interativas com Python."
)

# Texto em markdown
texto_markdown = "### Este é um texto em **markdown**!"

# Fórmula em LaTeX
formula_latex = r""" e^{i\pi} + 1 = 0 """

# Código
codigo_exemplo = "x = 42"

# 2. Exibição de Dados
subcabecalho_dados = "Exibição de Dados"

# Dados do DataFrame
data = {"A": [1, 2, 3, 4], "B": [10, 20, 30, 40]}
df = pd.DataFrame(data)

# JSON
json_exemplo = {"name": "Streamlit", "type": "Web Framework"}

# CSV como string
csv_exemplo = df.to_csv(index=False)

# Lista
lista_exemplo = [1, 2, 3, 4, 5]

# 3. Métricas
subcabecalho_metricas = "Métricas"

# Métricas com delta
temperatura = {"label": "Temperatura", "value": "70 °F", "delta": "1.2 °F"}
umidade = {"label": "Umidade", "value": "60%", "delta": "-5%"}
vento = {"label": "Velocidade do Vento", "value": "15 km/h", "delta": "2 km/h"}
ruido = {"label": "Nível de Ruído", "value": "40 dB", "delta": "1.5 dB"}
pressao = {
    "label": "Pressão Atmosférica",
    "value": "1013 hPa",
    "delta": "2 hPa",
}

# Métrica sem delta
populacao = {"label": "População", "value": "8 bilhões"}

# 4. Gráficos
subcabecalho_graficos = "Gráficos"

# Dados dos gráficos
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# Mais exemplos de gráficos
mais_graficos = "Mais Exemplos de Gráficos"

# Dados do gráfico de dispersão
scatter_data = pd.DataFrame(np.random.randn(100, 2), columns=["x", "y"])

# Dados do histograma
hist_data = np.random.randn(1000)

# 5. Mapas
subcabecalho_mapas = "Mapas"

# Dados do mapa
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

# 6. Mídia
subcabecalho_midia = "Mídia"

# URL da imagem
imagem_url = "https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png"
imagem_legenda = "Streamlit Logo"

# URL do áudio
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"

# URL do vídeo
video_url = "https://www.youtube.com/watch?v=B2iAodr0fOo"

# 7. Widgets
subcabecalho_widgets = "Widgets"

# Botão
botao = "Clique aqui"
botao_mensagem = "Botão clicado!"

# Checkbox
checkbox_label = "Eu aceito os termos e condições"

# Radio
radio_label = "Escolha uma opção"
radio_options = ("Opção 1", "Opção 2", "Opção 3")

# Selectbox
selectbox_label = "Selecione uma opção"
selectbox_options = ["Opção A", "Opção B", "Opção C"]

# Multiselect
multiselect_label = "Selecione múltiplas opções"
multiselect_options = ["Opção 1", "Opção 2", "Opção 3"]

# Slider
slider_label = "Selecione um valor"
slider_min = 0
slider_max = 100
slider_default = 50

# Select Slider
select_slider_label = "Selecione um intervalo"
select_slider_options = ["a", "b", "c", "d"]
select_slider_default = ("b", "c")

# Text Input
text_input_label = "Digite seu nome"

# Number Input
number_input_label = "Selecione um número"
number_input_min = 0
number_input_max = 100

# Text Area
text_area_label = "Escreva um texto"

# Date Input
date_input_label = "Selecione uma data"
date_input_default = datetime.now()

# Sidebar
sidebar_title = "Barra Lateral"
sidebar_button_label = "Botão na Barra Lateral"
sidebar_button_message = "Botão na barra lateral clicado!"

# Carregar CSV
subcabecalho_csv = "Carregar CSV"
file_uploader_label = "Escolha um arquivo CSV"
file_uploader_type = "csv"


# Função para converter DataFrame para Parquet
@st.cache_data
def convert_df_to_parquet(df):
    output = io.BytesIO()
    df.to_parquet(output, index=False)
    return output.getvalue()


download_button_label_parquet = "Baixar dados como Parquet"
download_button_filename_parquet = "dados.parquet"
download_button_mime_parquet = "application/octet-stream"
