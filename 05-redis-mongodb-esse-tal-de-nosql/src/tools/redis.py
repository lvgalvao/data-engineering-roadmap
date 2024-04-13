import os
import redis


class RedisClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RedisClient, cls).__new__(cls, *args, **kwargs)
            cls._instance._redis_client = cls._instance._connect_to_redis()
        return cls._instance

    @staticmethod
    def _load_config():
        return {
            "host": os.getenv("REDIS_HOST","localhost"),
            "port": os.getenv("REDIS_PORT",6379),
            "decode_responses": True
        }

    @classmethod
    def _connect_to_redis(cls):
        config = cls._load_config()
        redis_client = redis.StrictRedis(**config)
        return redis_client

    @classmethod
    def get(cls):
        return cls()._redis_client