"""
Closure is an inner function that remembers and has access to variables
in the local scope in which it was created, even after the outer function has
finish executing.
"""


# first example
def out_function():
    message = 'Hi'

    def in_function():
        print(message)

    # return in_function()  # for execute function
    return in_function


# out_function()  # normal
# out_function()()  # like auto invoke function
my_function = out_function()
my_function()

print('---')


# second example with params
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function()


hello_func = outer_function
hello_func("Hello")

bye_func = outer_function
bye_func("Bye")
