import logging
from time import time

logging.basicConfig(level=logging.DEBUG, filename='app_log.log', filemode='w')


def timer(function):
    def wrapper(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        logging.info(f"execution time: {end - start}; function: {function.__name__}; params: {args, kwargs}")
        return result

    return wrapper


def logger(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        logging.info(f"{result}")
        return result

    return wrapper
