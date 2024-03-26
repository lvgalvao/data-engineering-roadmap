import time
from functools import wraps

def retry(exception_to_check, tries=3, delay=1, backoff=2):
    """
    Decorator que retenta a função várias vezes em caso de exceção.
    
    :param exception_to_check: A exceção (ou tuple de exceções) que deve ser capturada.
    :param tries: O número máximo de tentativas.
    :param delay: O tempo de espera inicial entre as tentativas.
    :param backoff: O fator pelo qual o atraso deve aumentar após cada tentativa.
    """
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exception_to_check as e:
                    print(f"{func.__name__} falhou, tentando novamente em {_delay} segundos. Tentativas restantes: {_tries - 1}")
                    time.sleep(_delay)
                    _tries -= 1
                    _delay *= backoff
            return func(*args, **kwargs)
        return wrapper_retry
    return decorator_retry