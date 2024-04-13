from datetime import datetime
import json

from bs4 import BeautifulSoup
import pandas as pd
import requests
from request.crawlers.default_crawler import AbstractCrawler


class GenericRequestCrawler(AbstractCrawler):
    def __init__(self, type):
        super().__init__()
        self.type = type

    def crawl(self,query):
        self.query = query
        self.configs = json.loads(self.get_steps(self.type))
        if self.configs is None:
            raise("Crawler Não configurado!")
        self.get_data()
        self.extraction()
        self.transform_to_df_and_improve()
        self.save_data(self.df)


    def get_data(self):
        url = f"{self.configs["link"]["path"]}{self.query.replace(' ', self.configs["link"]["connector"])}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers)

        if response.status_code > 400:
            raise("Status Code != 200")    
        
        self.data = response.text
        

    def extraction(self):
        soup = BeautifulSoup(self.data, "html.parser")
        
        if self.configs["search"]["custom"]:
            results = soup.find_all(self.configs["search"]["tag"], self.configs["search"]["custom"])
        else:
            results = soup.find_all(self.configs["search"]["tag"], class_=self.configs["search"]["class"])

        data = []
        for result in results:
            product = {}
            for step in self.configs["product"]:
                value = self.configs["product"][step]
                try:
                    content = eval(value)
                except:
                    content = None
                product[step] = content
            data.append(product)
        self.df = data

    def transform_to_df_and_improve(self):
        df = pd.DataFrame(self.df)
        df = df.assign(keyword=self.query)
        df = df.assign(ecommerce = self.type)
        df = df.assign(dateTimeReference=datetime.now().isoformat())
        df = df.assign(crawlerType = "Request")
        self.df = df
