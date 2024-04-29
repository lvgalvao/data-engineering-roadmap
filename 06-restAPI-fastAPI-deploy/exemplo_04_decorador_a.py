import time
from functools import wraps

def alou_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            print("alou")
            time.sleep(1)
            result = func(*args, **kwargs)
            return result
    return wrapper