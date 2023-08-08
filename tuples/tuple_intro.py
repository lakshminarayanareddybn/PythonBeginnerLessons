# What is tuple?
# Tuples are used to store multiple items in a single variable
# Tuple is a collection which is ordered and unchangeable

var = 5
print(var)

# to modify value of the variable var is reassign with new value
var = 6
print(var)

my_tuple = (2,3,4,5,6)  # Tuples are defined with round brackets
print(my_tuple)

# We cant remove or add new elements to tuple directly

# Slicing or range indexing
# Access items of tuple
print(my_tuple[0])
print(my_tuple[0:3])
print(my_tuple[::-1])

# Tuples allows duplicate values
my_tuple1 = ("banana", "apple", "banana")
print(my_tuple1)

# How many times banana is repeated in tuple "my_tuple1"
print(my_tuple1.count("banana"))


tuple1 = (2,3,4,5)
tuple2 = (6,7,8,9)

print(type(tuple1))
print(type(tuple2))

result = tuple1 + tuple2
print(type(result))
print(result)

# Get the index of value
print(my_tuple1.index("banana"))


#         tuple1 = (   2,   3,   4,  5  ) 
# forward indexing :   0    1    2   3
# backward indexing : -4   -3   -2  -1  
print(tuple1[0])
print(tuple1[-4])
