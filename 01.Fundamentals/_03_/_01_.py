def greeting(name):
	print(f'Hello {name}')


def something(a_parameter):
	print(f'Interesting message for the masses {a_parameter}')

if __name__ == '__main__':
        greeting(input('What is your name?'))
        something(input('Just stesting something - texting something: '))