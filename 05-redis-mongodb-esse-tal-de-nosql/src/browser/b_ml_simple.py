from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

class MercadoLivreCrawler:
    def __init__(self):
        # Configurando as opções do Chrome para rodar headless
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")  # Rodar o Chrome em modo headless
        self.chrome_options.add_argument("--no-sandbox")  # Evitar problemas de sandbox
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--disable-setuid-sandbox")
        self.chrome_options.add_argument("--disable-web-security")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--memory-pressure-off")
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_argument("--disable-features=site-per-process")

        # Inicializando o driver do Chrome
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def execute_command(self, query):
        # Navegando para a página de pesquisa do Mercado Livre
        self.driver.get(f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}")
        
        # Aguardando um momento para a página carregar completamente
        time.sleep(5)

        # Obtendo o HTML da página
        html = self.driver.page_source

        # Analisando o HTML com BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")

        # Extraindo os dados que você deseja
        results = soup.find_all("div", class_="ui-search-result")

        data = []
        for result in results:
            # Aqui você pode extrair informações específicas de cada resultado, como título, preço, etc.
            link = None
            title = result.find("h2", class_="ui-search-item__title").text.strip()
            price = result.find("span", class_="andes-money-amount__fraction").text.strip()
            link_tag =  result.find("a", class_="ui-search-link")
            if link_tag:
                link = link_tag.get("href")
            data.append({"Produto": title, "Preço": price, "URL": link})

        # Fechando o navegador
        self.driver.quit()

        return data

    def send_dataframe(self, query):
        data = self.execute_command(query)
        df = pd.DataFrame(data)
        return df

# Exemplo de utilização
crawler = MercadoLivreCrawler()
dataframe = crawler.send_dataframe("fire emblem warriros")
print(dataframe)
