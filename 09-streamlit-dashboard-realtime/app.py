import pandas as pd
import streamlit as st

# Título da aplicação
st.title("Exemplo de Aplicação Streamlit")

# Adiciona um cabeçalho
st.header("Introdução ao Streamlit")

# Adiciona um texto
st.text("Esta é uma aplicação web criada com Streamlit!")

# Cria um dataframe
data = pd.DataFrame({"Coluna 1": [1, 2, 3, 4], "Coluna 2": [10, 20, 30, 40]})

# Exibe o dataframe
st.dataframe(data)

# Adiciona um gráfico de linha
st.line_chart(data)

# Adiciona um botão e uma resposta ao clique
if st.button("Clique aqui"):
    st.write("Botão clicado!")

# Adiciona um seletor
opcao = st.selectbox("Escolha uma opção", ["Opção A", "Opção B", "Opção C"])
st.write("Você selecionou:", opcao)
