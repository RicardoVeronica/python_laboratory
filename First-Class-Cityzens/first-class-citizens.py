"""
First class functions, First class cityzens, first class order
functions or First class objects, is an entity which supports all the
operations generally available to other entities.
This options typically include being passed as an argument, returned from a
function and assigned to a variable.
Functions have the same characteristics as values like string or numbers.
"""


def square(x):
    """
    Retrieve the square of a number
    """
    return x ** 2


# Assign a function to a variable
func = square
print(func)
print(f"\nThis is the result = {func(9)}")

# Function are like other data-type for instance a list item
lst = [1, "hello", func]
print(f"This is the result in a list = {lst[2](9)}")


print('\n---\n')


def cube(x):
    """
    Retrieve the cube of a number
    """
    return x ** 3


# Pass a function like an argument of another function
def my_map(func, arg_list):
    """
    Retrurn the arg_list apply the func in first arg
    """
    result = []

    for item in arg_list:
        result.append(func(item))

    return result


squares = my_map(cube, [2, 3, 4, 5, 6])
print(f'This is the result for my_map function: {squares}')

print('\n---\n')


# Return a function for another function
def logger(msg):
    def log_message():
        print('Log:', msg)

    return log_message


log_hi = logger('Hi people')
log_hi()

print('\n---\n')


# Return a function for another function, html example
def html(tag):
    def wrap_txt(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_txt


h1 = html('h1')
h1('Header')

p = html('p')
p('Paragraph')
