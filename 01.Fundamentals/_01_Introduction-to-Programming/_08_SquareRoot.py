import math


def print_square_root(number):
    sqrt_of_number = math.sqrt(number)
    print('{0:.2F}'.format(sqrt_of_number))


number = int(input('Enter a number of which you want to find out the square root of: '))
print_square_root(number)

