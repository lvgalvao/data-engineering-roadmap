from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True  # Executar em modo headless
    driver = webdriver.Firefox(options=options)
    # Iniciar o WebDriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)

def test_check_title_is(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    # Verifica se o titulo de página é
    sleep(2)
    # Capturar o título da página
    page_title = driver.title

    # Verificar se o título da página é o esperado
    expected_title = "Validador de schema excel"  # Substitua com o título real esperado
    assert page_title == expected_title

def test_check_streamlit_h1(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(2)  # Espera 5 segundos

    # Capturar o primeiro elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Insira o seu excel para validação"
    assert h1_element.text == expected_text

def test_check_usuario_pode_inserir_um_excel_e_receber_uma_mensagem(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(3)  # Espera 5 segundos

    # Realizar o upload do arquivo de sucesso
    success_file_path = os.path.abspath("data/correto.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

    # Aguardar a mensagem de sucesso
    sleep(3)
    assert "O schema do arquivo Excel está correto!" in driver.page_source

def test_check_mais_de_uma_mensagem_de_erro(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(3)  # Espera 5 segundos

    # Realizar o upload do arquivo de sucesso
    multiple_erros_file_path = os.path.abspath("data/multiplos_erros.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(multiple_erros_file_path)

    # Aguardar a mensagem de sucesso
    sleep(3)
    # Localizar todas as ocorrências da mensagem de erro
    error_messages = driver.find_elements(By.XPATH, "//*[contains(text(), 'Erro na validação')]")

    # Verificar se existem pelo menos duas mensagens de erro
    assert len(error_messages) == 2, f"Quantidade de mensagens de erro encontradas: {len(error_messages)}"

def test_check_usuario_insere_um_excel_valido_e_aparece_um_botao(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(3)  # Espera 3 segundos

    # Realizar o upload do arquivo de sucesso
    success_file_path = os.path.abspath("data/correto.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

    # Aguardar a mensagem de sucesso
    sleep(3)
    assert "O schema do arquivo Excel está correto!" in driver.page_source
    # Verificar se o botão "Salvar no Banco de Dados" está presente
    buttons = driver.find_elements(By.XPATH, "//button")
    save_button = None
    for button in buttons:
        if button.text == "Salvar no Banco de Dados":
            save_button = button
            break

    assert save_button is not None and save_button.is_displayed()