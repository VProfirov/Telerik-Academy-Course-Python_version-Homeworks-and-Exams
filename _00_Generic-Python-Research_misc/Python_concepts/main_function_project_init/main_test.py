print('\n')
print(f'The __name__ of main_test.py is: {__name__}')
print('\n')


def print_function():
    print('\n')
    print(f'FROM FUNCTION: The __name__ of main_test.py is: {__name__}')
    print('\n')


def some_function():
    print('I AM SOME FUNCTION')


def some_function2():
    print('I AM SOME FUNCTION NUM 2')


if __name__ == '__main__':
    print('if __name__ == __main__  ++--')


some_function2()
