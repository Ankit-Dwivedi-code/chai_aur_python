# Create a function that accepts any number of keyword arguments and prints them in the format key: value

def func(**kwargs):
    for k, v in kwargs.items(): print(f'{k}: {v}')

func(a=10, b='Hello', c=[1, 2])
# func(1) error