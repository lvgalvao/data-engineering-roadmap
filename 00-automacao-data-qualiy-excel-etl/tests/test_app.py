import pytest
import subprocess
import time
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciar o WebDriver (ajuste o caminho se necessário)
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
