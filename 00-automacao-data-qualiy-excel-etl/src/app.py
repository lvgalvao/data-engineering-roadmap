from frontend import ExcelValidatorUI
from backend import process_excel

def main():
    """
    Função principal para executar a aplicação de validação de arquivos Excel.

    Esta função cria uma interface de usuário (UI), permite que o usuário selecione
    um modelo de dados e faça o upload de um arquivo Excel. O arquivo é então processado
    e os resultados são exibidos na UI.
    """
    ui = ExcelValidatorUI()
    ui.display_header()

    model_choice = ui.select_model()
    uploaded_file = ui.upload_file()

    if uploaded_file is not None:
        result, error = process_excel(uploaded_file, model_choice)
        ui.display_results(result, error)

if __name__ == "__main__":
    main()