from time import time, sleep
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("{}: {:.2f}s".format(func.__name__, end - start))
        return result

    return wrapper


@timer
def timer_test():
    sleep(2)


if __name__ == "__main__":
    timer_test()
