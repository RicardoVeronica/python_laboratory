"""
Decorator is a function that change the functionality of another function
"""


# first example
def decorator_function(msg):
    def wrapper_function(another_msg):
        print(msg + ' ' + another_msg)

    return wrapper_function


my_func = decorator_function('Hello world')
my_func('Hello again')

print('---')


# example with numbers and args
def decorator_function(num1, num2):
    add = num1 + num2

    def wrapper_function(num3):
        print(add / num3)

    return wrapper_function


this_func = decorator_function(5, 8)
this_func(2)

print('---')


# example correctly executed
def decorator_function(original_func):
    # here add more funcionality to the original_func
    print(f'Wrapper execute this before {original_func.__name__} function')

    def wrapper_function():
        return original_func()  # execute the original_func + upper code

    return wrapper_function


@decorator_function
def display():
    print('display function execution')


# this 2 lines change for the @decorator_function syntax
# decorated_display = decorator_function(display)
# decorated_display()
display()
