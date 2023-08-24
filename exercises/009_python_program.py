## Bitwise operators

decimal_num_1 = 7 # Decimal number format
binary_num_1 = bin(decimal_num_1)
octal_num_1 = oct(decimal_num_1)
hex_num_1 = hex(decimal_num_1)

print(f"Decimal number: {decimal_num_1}")
print(f"Binary number: {binary_num_1}")
print(f"Octal number: {octal_num_1}")
print(f"Hex number: {hex_num_1}")

# 11010 # binary format.
# convert this to other 3 number systems
binary_num_2 = 0b11010
decimal_num_2 = int(binary_num_2)
octal_num_2 = oct(binary_num_2)
hex_num_2 = hex(binary_num_2)

print("+++++++++++++++++++++++++++++\n\n")
print(f"Decimal number: {decimal_num_2}")
print(f"Binary number: {binary_num_2:b}")
print(f"Octal number: {octal_num_2}")
print(f"Hex number: {hex_num_2}")

