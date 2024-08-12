# Create a decorator to print the function name and the values of its arguments every time the function is called.

def print_func(function):
    def wrapper(*args, **kwargs):
        print("Function Name:", function.__name__)
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{key}={value}" for key, value in kwargs.items())
        
        if args_val and kwargs_val:
            print(f"Function Arguments: ({args_val}, {kwargs_val})")
        elif args_val:
            print(f"Function Arguments: ({args_val})")
        elif kwargs_val:
            print(f"Function Arguments: ({kwargs_val})")
        else:
            print("Function Arguments: ()")
        
        return function(*args, **kwargs)
    return wrapper

@print_func
def func1(name, greeting="Hello"):
    print(greeting, name)

func1("Ankit", greeting="Hi")


@print_func
def func2(a, b, c="default"):
    print(a, b, c)

func2(1, 2)
# func2(1, 2, c="changed")
