'''
Currently using Python3.x (3.9)
There is no limit to the builtin datatypes. The only limit speculated is the size of the RAM available.
Checking for 'max' size of int for example: will give different number depending on the system run and adding (+1) doesn't overload it,
the way it happens in languages like C#(9) ofr example.

Also the type handling in python is implicit( in this case, namely int and float numbers) and inferred by the litteral's value.
'''
numbers = [52130, -115, 4825932, 97, -10000]
numbers[0]
numbers[1]
# will have the same functionality as:
num1 = 52130
num2 = -115

print(type(numbers))
print(type(numbers[0]))
print(type(num1))