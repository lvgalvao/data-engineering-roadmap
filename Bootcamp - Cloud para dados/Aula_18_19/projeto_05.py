import streamlit as st
import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configuração do banco de dados
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Função para conectar ao banco
def connect_to_database():
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para inserir dados
def insert_data(nome, idade):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
            conn.commit()
            st.success(f"Dados inseridos: {nome}, {idade} anos")
        except Exception as e:
            st.error(f"Erro ao inserir dados: {e}")
        finally:
            conn.close()

# Interface Streamlit
st.title("Inserção de Dados no Banco de Dados SQL")

nome = st.text_input("Nome:")
idade = st.number_input("Idade:", min_value=0, step=1)

if st.button("Inserir Dados"):
    if nome and idade:
        insert_data(nome, idade)
    else:
        st.warning("Preencha todos os campos.")
