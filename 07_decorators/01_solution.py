import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time() - start
        print('{} took {} seconds'.format(func.__name__, end))
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(5)

slow_function()

