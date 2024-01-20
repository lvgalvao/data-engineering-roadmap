import streamlit as st

def set_page_config():
    st.set_page_config(page_title="Validador de Schema de Excel", layout="wide")

def show_ui():
    st.title("Validador de Schema de Excel")
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])
    return uploaded_file

def display_results(result, error):
    if error:
        st.error(f"Erro na validação: {error}")
    else:
        st.success("O schema do arquivo Excel está correto!")