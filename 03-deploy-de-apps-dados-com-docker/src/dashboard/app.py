# dashboard/app.py
import streamlit as st
import duckdb
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as variáveis de ambiente
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

st.title('Dashboard de Dados')

# Cria a conexão com DuckDB em memória
con = duckdb.connect(database=':memory:', read_only=False)

# Instala e carrega a extensão Postgres no DuckDB
con.execute("INSTALL 'postgres';")
con.execute("LOAD 'postgres';")

# Conexão com o banco de dados PostgreSQL utilizando as variáveis de ambiente
pg_connection_string = f"host={DB_HOST} port={DB_PORT} dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD}"

# Anexa o banco de dados PostgreSQL ao DuckDB
con.execute(f"ATTACH '{pg_connection_string}' AS pg_db (TYPE 'postgres');")

# Agora você pode realizar consultas SQL como se as tabelas do PostgreSQL fossem tabelas do DuckDB
result = con.execute("SELECT * FROM pg_db.public.my_table;").fetchall()

# Exibe o resultado no Streamlit
st.write(result)
