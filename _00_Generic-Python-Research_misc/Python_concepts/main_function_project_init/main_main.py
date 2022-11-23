import main_test

print('\n')
print(f'The __name__ of main_main.py is: {__name__}')
print('\n')

main_test.some_function()


print(f'Inner functions and properties:')
print(f'__name__ : {__name__}')
# print(f'__path__ : {__path__}')
print(f'__doc__ : {__doc__}')
# print(f'__qualname__ : {__qualname__}')
print(f'__package__ : {__package__}')
print(f'__spec__ : {__spec__}')