##https://json-ld.org/learn.html
import time
import json
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from browser.crawlers.default_crawler import AbstractCrawler
from browser.provider.actions.dict import action_dict

class GenericBrowserCrawler(AbstractCrawler):
    def __init__(self, type):
        super().__init__()
        self.type = type
        self.steps = json.loads(self.get_steps(self.type))
        if self.steps is None:
            raise("Crawler Não configurado!")

    def crawl(self, query):
        self.query = query
        self.execute_before()
        df = self.execute_main()
        self.execute_after()
        self.mongo.save_dataframe(df)
        print("Wait")
        
    def execute_main(self):
        self.browser.get(f"{self.steps["link"]["path"]}{self.query.replace(' ', self.steps["link"]["connector"])}")
        time.sleep(5)
        self.content = self.extraction()
        self.browser.quit()
        return self.transform_to_df_and_improve(self.content)    
    
    def execute_before(self):
        before = self.steps["script"]["before"]
        if before:
            for action in before:
                if action_dict[action] is None:
                    raise("Script não definido")
                action_dict[action](self.browser, before[action])
            return

    def execute_after(self):
        after = self.steps["script"]["after"]
        if after:
            for action in after:
                if action_dict[action] is None:
                    raise("Script não definido")
                action_dict[action](self.browser, after[action])
            return

    def extraction(self):
        self.html = self.browser.page_source
        
        soup = BeautifulSoup(self.html, "html.parser")
        
        if self.steps["search"]["custom"]:
            results = soup.find_all(self.steps["search"]["tag"], self.steps["search"]["custom"])
        else:
            results = soup.find_all(self.steps["search"]["tag"], class_=self.steps["search"]["class"])

        data = []
        for result in results:
            product = {}
            for step in self.steps["product"]:
                value = self.steps["product"][step]
                try:
                    content = eval(value)
                except:
                    content = None
                product[step] = content
            data.append(product)
        return data

    def transform_to_df_and_improve(self, data):
        df = pd.DataFrame(data)
        df = df.assign(keyword=self.query)
        df = df.assign(ecommerce = self.type)
        df = df.assign(dateTimeReference=datetime.now().isoformat())
        df = df.assign(crawlerType = "Browser")
        return df

