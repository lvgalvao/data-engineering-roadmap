from frontend import ExcelValidatorUI
from backend import process_excel

def main():

    ui = ExcelValidatorUI()
    ui.display_header()

    model_choice = ui.select_model()
    uploaded_file = ui.upload_file()

    if uploaded_file is not None:
        result, error = process_excel(uploaded_file, 
                                      model_choice)
        ui.display_results(result, error)

if __name__ == "__main__":
    main()