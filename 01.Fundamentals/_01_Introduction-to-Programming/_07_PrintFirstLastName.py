def print_first_last_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name)


first_last_name = input("Enter your First and Last name: ").split(" ")
first_name = first_last_name[0]
last_name = first_last_name[1]
print_first_last_name(first_name, last_name)


print(first_name)
print(last_name)
