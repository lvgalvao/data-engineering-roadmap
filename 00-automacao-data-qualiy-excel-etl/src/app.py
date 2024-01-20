# from frontend import show_ui, display_results, set_page_config
from frontend import ExcelValidatorUI
from backend import process_excel

def main():
    # set_page_config()
    ui = ExcelValidatorUI("Validador de Schema de Excel")
    # uploaded_file = show_ui()
    arquivo_excel_carregado = ui.upload_file()

    if arquivo_excel_carregado is not None:
        result, error = process_excel(arquivo_excel_carregado)
        # display_results(result, error)
        ui.display_results(result, error)

if __name__ == "__main__":
    main()