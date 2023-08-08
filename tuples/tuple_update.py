my_tuple = (2,3,4,5)
print(my_tuple)

my_list = list(my_tuple)
print(my_list)

my_list.append(6)
my_list.append(7)
my_list.append(8)
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

# del my_tuple[0]
my_list = list(my_tuple)
del my_list[0]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

