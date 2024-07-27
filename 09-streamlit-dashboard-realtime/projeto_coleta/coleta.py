import pandas as pd
import streamlit as st

# Título do aplicativo
st.title("Coleta de Dados da Enquete")

# Nome do arquivo CSV onde os dados serão armazenados
data_file = "survey_data.csv"

data = pd.DataFrame(
    columns=[
        "Estado",
        "Nível de Experiência",
        "Bibliotecas",
        "Área de Atuação",
        "Horas de Estudo",
        "Conforto com Dados",
        "Experiência de Python",
        "Experiência de SQL",
        "Experiência em Cloud",
    ]
)

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
        ["Desconfortável", "Neutro", "Confortável", "Muito Confortável"],
    )
    experiencia_python = st.slider("Experiência de Python", 0, 10)
    experiencia_sql = st.slider("Experiência de SQL", 0, 10)
    experiencia_cloud = st.slider("Experiência em Cloud", 0, 10)

    # Botão para submeter o formulário
    submit_button = st.form_submit_button(label="Enviar")

# Se o botão foi clicado, salvar os dados no DataFrame
if submit_button:
    novo_dado = {
        "Estado": estado,
        "Bibliotecas e ferramentas": ", ".join(bibliotecas_selecionadas),
        "Área de Atuação": area_atuacao,
        "Horas de Estudo": horas_codando,
        "Conforto com Dados": conforto_dados,
        "Experiência de Python": experiencia_python,
        "Experiência de SQL": experiencia_sql,
        "Experiência em Cloud": experiencia_cloud,
    }
    data = data.append(novo_dado, ignore_index=True)
    data.to_csv(data_file, index=False)
    st.success("Dados enviados com sucesso!")
