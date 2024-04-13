from abc import ABC, abstractmethod

from browser.provider.generic_b_crawler import GenericBrowserCrawler
from tools.redis import RedisClient
from tools.mongodb import MongoConnection


class AbstractCrawler(ABC):
    def __init__(self):
        self.redis = RedisClient.get()
        self.mongo = MongoConnection()

    @abstractmethod
    def crawl(self):
        pass

    def get_steps(self, site):
        return self.redis.get(site)
    
    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except:
            raise("Não foi possível salvar os dados no Mongo")