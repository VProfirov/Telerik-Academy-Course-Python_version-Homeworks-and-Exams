def print_name(name):
    print("Hello, " + name + ".")


if __name__ == '__main__':
    name = 'Pesho Peshev'
    input_user_name = input('Enter user name: ')
    if input_user_name:
        name = input_user_name
    print_name(name)
