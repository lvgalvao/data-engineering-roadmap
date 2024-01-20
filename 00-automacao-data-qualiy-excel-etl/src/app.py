from frontend import show_ui, display_results, set_page_config
from backend import process_excel

def main():
    set_page_config()
    uploaded_file = show_ui()

    if uploaded_file is not None:
        result, error = process_excel(uploaded_file)
        display_results(result, error)

if __name__ == "__main__":
    main()