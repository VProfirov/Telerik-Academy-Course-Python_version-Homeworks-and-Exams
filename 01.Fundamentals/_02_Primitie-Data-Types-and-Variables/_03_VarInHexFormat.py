# convert int(254) in to hex()

int_number = 254
hex_number = hex(int_number)
int_from_hex_number = int(hex_number, 16)

print(f'int: {int_number} => hex: {hex_number} => int: {int_from_hex_number}')