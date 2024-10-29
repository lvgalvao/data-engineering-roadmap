import streamlit as st

# Título do aplicativo
st.title("Hello, World! com Streamlit")

# Exibindo uma mensagem de boas-vindas
st.write("Este é um exemplo simples de uma aplicação Streamlit em Docker.")

# Adicionando um botão de interação
if st.button("Clique aqui"):
    st.success("Você clicou no botão!")
