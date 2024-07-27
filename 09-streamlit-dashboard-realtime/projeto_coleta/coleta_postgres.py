import os

import psycopg2
import streamlit as st
from dotenv import load_dotenv
from psycopg2 import sql

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


# Conectar ao banco de dados PostgreSQL
def conectar_banco():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Função para criar a tabela caso não exista
def criar_tabela_se_nao_existir(conn):
    try:
        with conn.cursor() as cur:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS survey_data (
                id SERIAL PRIMARY KEY,
                estado VARCHAR(50),
                bibliotecas TEXT,
                area_atuacao VARCHAR(50),
                horas_estudo VARCHAR(20),
                conforto_dados VARCHAR(50),
                experiencia_python INTEGER,
                experiencia_sql INTEGER,
                experiencia_cloud INTEGER
            )
            """
            cur.execute(create_table_query)
            conn.commit()
    except Exception as e:
        st.error(f"Erro ao criar a tabela: {e}")


# Função para salvar dados no banco de dados
def salvar_dados_banco(conn, dados):
    try:
        with conn.cursor() as cur:
            insert_query = sql.SQL("""
                INSERT INTO survey_data (estado, bibliotecas, area_atuacao, horas_estudo, conforto_dados, experiencia_python, experiencia_sql, experiencia_cloud)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """)
            cur.execute(
                insert_query,
                (
                    dados["Estado"],
                    dados["Bibliotecas e ferramentas"],
                    dados["Área de Atuação"],
                    dados["Horas de Estudo"],
                    dados["Conforto com Dados"],
                    dados["Experiência de Python"],
                    dados["Experiência de SQL"],
                    dados["Experiência de Cloud"],
                ),
            )
            conn.commit()
    except Exception as e:
        st.error(f"Erro ao salvar os dados no banco de dados: {e}")


# Título do aplicativo
st.title("Coleta de Dados da Enquete")

# Opções de bibliotecas
bibliotecas = [
    "Pandas",
    "Pydantic",
    "scikit-learn",
    "Git",
    "Pandera",
    "streamlit",
    "postgres",
    "databricks",
    "AWS",
    "Azure",
    "airflow",
    "dbt",
    "Pyspark",
    "Polars",
    "Kafka",
    "Duckdb",
    "PowerBI",
    "Excel",
    "Tableau",
    "storm",
]

# Formulário para entrada de dados
with st.form("dados_enquete"):
    estado = st.selectbox(
        "Estado",
        [
            "Acre",
            "Alagoas",
            "Amapá",
            "Amazonas",
            "Bahia",
            "Ceará",
            "Distrito Federal",
            "Espírito Santo",
            "Goiás",
            "Maranhão",
            "Mato Grosso",
            "Mato Grosso do Sul",
            "Minas Gerais",
            "Pará",
            "Paraíba",
            "Paraná",
            "Pernambuco",
            "Piauí",
            "Rio de Janeiro",
            "Rio Grande do Norte",
            "Rio Grande do Sul",
            "Rondônia",
            "Roraima",
            "Santa Catarina",
            "São Paulo",
            "Sergipe",
            "Tocantins",
        ],
    )
    area_atuacao = st.selectbox(
        "Área de Atuação",
        ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"],
    )
    bibliotecas_selecionadas = st.multiselect(
        "Bibliotecas e ferramentas mais utilizadas", bibliotecas
    )
    horas_codando = st.selectbox(
        "Horas Codando ao longo da semana",
        ["Menos de 5", "5-10", "10-20", "Mais de 20"],
    )
    conforto_dados = st.selectbox(
        "Conforto ao programar e trabalhar com dados",
        [
            "Muito Desconfortável",
            "Desconfortável",
            "Neutro",
            "Confortável",
            "Muito Confortável",
        ],
    )
    experiencia_python = st.slider("Experiência de Python", 0, 10)
    experiencia_sql = st.slider("Experiência de SQL", 0, 10)
    experiencia_cloud = st.slider("Experiência em Cloud", 0, 10)

    # Botão para submeter o formulário
    submit_button = st.form_submit_button(label="Enviar")

# Se o botão foi clicado, salvar os dados no DataFrame e no banco de dados
if submit_button:
    novo_dado = {
        "Estado": estado,
        "Bibliotecas e ferramentas": ", ".join(bibliotecas_selecionadas),
        "Área de Atuação": area_atuacao,
        "Horas de Estudo": horas_codando,
        "Conforto com Dados": conforto_dados,
        "Experiência de Python": experiencia_python,
        "Experiência de SQL": experiencia_sql,
        "Experiência de Cloud": experiencia_cloud,
    }

    conn = conectar_banco()
    if conn:
        criar_tabela_se_nao_existir(conn)
        salvar_dados_banco(conn, novo_dado)
        conn.close()

    st.success("Dados enviados com sucesso!")
