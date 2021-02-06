print('\n')
print(f'The __name__ of main_test.py is: {__name__}')
print('\n')

def print_function():
    print('\n')
    print(f'FROM FUNCTION: The __name__ of main_test.py is: {__name__}')
    print('\n')

def some_function():
    print('I AM SOME FUNCTION')

if __name__ == '__main__':
    print_function()