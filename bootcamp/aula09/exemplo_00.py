from log import log_decorator

from timer import time_measure_decorator

from hello import hello


@hello
def soma_1(a, b):
    return a + b

soma_1(1,2)