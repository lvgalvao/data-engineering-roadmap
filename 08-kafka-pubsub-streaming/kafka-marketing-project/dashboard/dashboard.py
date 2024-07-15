import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import time
import plotly.express as px

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do PostgreSQL
db_url = 'postgresql://postgres_kafka_user:UQ4PAxSQbukeWVcFEDpdNquS6zhbt8zs@dpg-cq8vi35ds78s7396a4og-a.oregon-postgres.render.com/postgres_kafka_sink'
engine = create_engine(db_url)

# Função para carregar dados do banco de dados
def load_data():
    query = """
    SELECT DISTINCT ON (id) *
    FROM temperature_data
    ORDER BY id, time DESC;
    """
    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

# Função para exibir o mapa
def display_map(df):
    df['color'] = df['temperature'].apply(lambda x: 'red' if x > 5 else 'blue')
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="color",
        color_discrete_map={"red": "red", "blue": "blue"},
        hover_name="id",
        hover_data={"temperature": True, "latitude": False, "longitude": False},
        zoom=3,
        height=600,
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig)

# Loop para atualizar a página a cada 5 segundos
while True:
    st.title('Dashboard de Temperaturas')
    data = load_data()
    if not data.empty:
        st.write(data)
        display_map(data)
    else:
        st.write('A tabela "temperature_data" ainda não existe ou não foi possível carregar os dados.')
    
    time.sleep(10)
    st.experimental_rerun
