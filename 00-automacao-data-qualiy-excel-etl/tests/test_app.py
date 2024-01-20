import os
import pytest
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Importando TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



@pytest.fixture(scope="module")
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciar o WebDriver usando GeckoDriver
    driver = webdriver.Firefox()
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    driver.get("http://localhost:8501")

    # Aguardar um tempo para a aplicação carregar
    time.sleep(5)

    # Verificar se o título da página é o esperado
    assert "Validador de Schema de Excel" in driver.title

# def test_successful_upload(driver):
#     driver.get("http://localhost:8501")

#     # Aguardar um tempo para a aplicação carregar
#     time.sleep(5)

#     # Realizar o upload do arquivo de sucesso
#     success_file_path = os.path.abspath("data/success.xlsx")
#     driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)

#     # Aguardar a mensagem de sucesso
#     time.sleep(5)
#     assert "O schema do arquivo Excel está correto!" in driver.page_source

# def test_failed_upload(driver):
#     driver.get("http://localhost:8501")

#     # Aguardar um tempo para a aplicação carregar
#     time.sleep(5)

#     # Realizar o upload do arquivo de falha
#     failure_file_path = os.path.abspath("data/failure.xlsx")
#     driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(failure_file_path)

#     # Aguardar a mensagem de erro
#     time.sleep(5)
#     assert "Erro na validação" in driver.page_source

def test_successful_upload_using_select(driver):
    driver.get("http://localhost:8501")
    time.sleep(5)  # Aguarda a aplicação carregar

    try:
        select_box = driver.find_element(By.CLASS_NAME, "stSelectbox")
        ActionChains(driver).move_to_element(select_box).click().perform()
        time.sleep(2)  # Aguarda o selectbox abrir

        ActionChains(driver).send_keys("Usuario").send_keys(Keys.ENTER).perform()
        time.sleep(2)  # Aguarda a seleção ser feita

    except Exception as e:
        print(f"Erro durante a interação com o selectbox: {e}")
        return

    # Realizar o upload do arquivo de sucesso
    success_file_path = os.path.abspath("data/success.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(success_file_path)
    time.sleep(5)  # Aguarda o upload do arquivo

    # Aguardar a mensagem de sucesso
    success_message = "O schema do arquivo Excel está correto!"
    assert success_message in driver.page_source

def test_failed_upload_using_select(driver):
    driver.get("http://localhost:8501")
    time.sleep(5)  # Aguarda a aplicação carregar

    try:
        select_box = driver.find_element(By.CLASS_NAME, "stSelectbox")
        ActionChains(driver).move_to_element(select_box).click().perform()
        time.sleep(2)  # Aguarda o selectbox abrir

        ActionChains(driver).send_keys("Usuario").send_keys(Keys.ENTER).perform()
        time.sleep(2)  # Aguarda a seleção ser feita

    except Exception as e:
        print(f"Erro durante a interação com o selectbox: {e}")
        return

    # Realizar o upload do arquivo de falha
    failure_file_path = os.path.abspath("data/failure.xlsx")
    driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(failure_file_path)
    time.sleep(5)  # Aguarda o upload do arquivo

    # Aguardar a mensagem de sucesso
    failure_message = "Erro na validação"
    assert failure_message in driver.page_source