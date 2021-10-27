from decorators_examples.decorators import decorator


@decorator
def add(a, b):
    print(f'The result is "{a + b}"')


@decorator
def sub(a, b):
    print(f'The result is "{a - b}"')


@decorator
def display_info(name, age, dictionary):
    print(f'display_info: {name}, {age}, {dictionary}')


if __name__ == '__main__':
    add(1, 2)
    print('---')
    sub(100, 20)
    print('---')
    display_info('Richard', 36, {'one': 1})
