import functools
import logging


def log(filename=None):
    """ автоматически логирует начало и конец выполнения функций,
    а также их результаты или возникшие ошибки,
    может записывать логи в файл или выводить их в консоль."""
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logging.info(f"Starting {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
