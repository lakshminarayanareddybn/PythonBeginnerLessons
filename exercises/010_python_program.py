## Examples on bitwise operations

# decimal numbers
a = 10
b = 4

# binary numbers
bin_a = bin(a)
bin_b = bin(b)
print(bin_a)
print(bin_b)

c = a & b
print(f"{c:b}")

# a : 1010
# b :  100
# a|b:1110
d = a | b
print(f"{d:b}")

# ####
#   A   B    &   |   ^ 
# ---------------------
#   0   0    0   0   0
#   0   1    0   1   1
#   1   0    0   1   1
#   1   1    1   1   0