def print_first_last_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name)


if __name__ == '__main__':
# no defaulting of input
    first_last_name = input("Enter your 'First Last' name: ").strip(' \t\n\r').split(' ')
    first_name = first_last_name[0]
    last_name = first_last_name[len(first_last_name) - 1]
    print_first_last_name(first_name, last_name)


