import time
from functools import wraps


def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[LOG] Запуск {func.__name__}")

        result = func(*args, **kwargs)

        end = time.time()
        print(f"[LOG] {func.__name__} выполнен за {end - start:.4f} сек")

        return result

    return wrapper