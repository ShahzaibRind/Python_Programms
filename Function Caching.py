import time
from functools import lru_cache

@lru_cache()
def some_work(n):
    # Some Task taking a seconds
    time.sleep(n)
    return n


if __name__ == '__main__':
    print('Now running some work...')
    some_work(3)
    print('Done... Calling again')
    some_work(3)
    print('Again Called.')
