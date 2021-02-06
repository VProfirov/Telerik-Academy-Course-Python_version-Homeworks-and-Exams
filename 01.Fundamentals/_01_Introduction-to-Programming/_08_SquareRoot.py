import math


def get_square_root(number):
    sqrt_of_number = math.sqrt(number)
    return sqrt_of_number


if __name__ == '__main__':
    number = int(input('Enter a number of which you want to find out the square root of: '))
    sqrt_number = get_square_root(number)
    print('{0:.2F}'.format(sqrt_number))
