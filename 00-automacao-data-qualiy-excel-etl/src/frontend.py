import streamlit as st

class ExcelValidatorUI:
    """
    Classe responsável por gerar a interface de usuário para o validador de arquivos Excel.
    """
    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(page_title="Validador de Schema de Excel", layout="wide")

    def display_header(self):
        st.title("Validador de Schema de Excel")

    def upload_file(self):
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["csv"])

    def display_results(self, result, error):
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto!")
