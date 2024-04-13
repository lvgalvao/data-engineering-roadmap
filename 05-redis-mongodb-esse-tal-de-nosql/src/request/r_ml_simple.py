import requests
from bs4 import BeautifulSoup
import pandas as pd

class MercadoLivreCrawler:
    def execute_command(self, query):
        url = f"https://lista.mercadolivre.com.br/{query.replace(' ', '-')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all("div", class_="ui-search-result")

            data = []
            for result in results:
                link = None
                title = result.find("h2", class_="ui-search-item__title").text.strip()
                price = result.find("span", class_="andes-money-amount__fraction").text.strip()
                link_tag =  result.find("a", class_="ui-search-link")
                if link_tag:
                    link = link_tag.get("href")
                data.append({"Produto": title, "Preço": price, "URL": link})

            return data
        else:
            print("Falha ao fazer a solicitação HTTP.")
            return None

    def send_dataframe(self, query):
        data = self.execute_command(query)
        if data:
            df = pd.DataFrame(data)
            return df
        else:
            return None

# Exemplo de utilização
crawler = MercadoLivreCrawler()
dataframe = crawler.send_dataframe("iphone 12")
if dataframe is not None:
    print(dataframe)
else:
    print("Erro ao obter os dados.")
