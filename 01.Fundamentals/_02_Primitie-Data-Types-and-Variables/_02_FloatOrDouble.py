# Float or double : 34.567839023, 12.345, 8923.1234857, 3456.091

'''
In Python there is only one built in datatype
that handle single point precision - float.

Python3.x has single floating number precision of (17-18) equivalent of C#9's double (16-17 symbols)
'''

float_numbers = [34.567839023,12.345,8923.1234857, 3456.091]
float_number_01 = 34.567839023

print(type(float_numbers))
print(type(float_numbers[0]))
print(type(float_number_01))
print(f'{float_numbers[0]} == {float_number_01} => {float_numbers[0] == float_number_01}')

float_large = 34.12345678912345678912345678900567839023567839023567839023567839023567839023091
print(f'Large float: {float_large}')
print(f'Large float number after devision: { float_large / 99999999999999999999}')

float_num_01 = 0.12345678912346789123456789
print(float_num_01)
print(f'Float (float_num_01) has precision of {len(str(float_num_01)) - 1}')


float_num_02 = 11.12345678912346789123456789
print(float_num_02)
print(f'Float (float_num_02) has precision of {len(str(float_num_02)) - 1}')

count = 0
print(f'------ FLOAT NUM_01 -------')
for i in str(float_num_01):
    count += 1
    print(f'[{count}] ==> {i}')


print(f'------ FLOAT NUM_02 -------')
count = 0
for i in str(float_num_02):
    count += 1
    print(f'[{count}] ==> {i}')
