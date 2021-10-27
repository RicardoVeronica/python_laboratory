def decorator(function):
    def wrapper(*args, **kwargs):
        print(f'Function "{function.__name__}" Start with arguments: {args}')
        function(*args, **kwargs)
        print(f'End function "{function.__name__}"')

    return wrapper


def function_decorator(original_func):
    print(f'Wrapper execute this before {original_func.__name__} function')

    def wrapper_function(*args, **kwargs):
        return original_func(*args, **kwargs)

    return wrapper_function
