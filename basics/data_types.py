# Text type : str

my_str_var = "hello"
print(type(my_str_var)) # <class 'str'>

if isinstance(my_str_var, str):
    print("my_str_var is of str datatype")
else:
    print("my_str_var is not a str dattype")
    
# # Numeric types: int, float, complex

num_one = 1 # int
float_one = 1.5 # float
complex_one = 1j

print(f"{num_one} is of {type(num_one)}")
print(f"{float_one} is of {type(float_one)}")
print(f"{complex_one} is of {type(complex_one)}")


# Boolean Type: bool
x = True
y = False
print(f"x={x} is of {type(x)}")
print(f"y={y} is of {type(y)}")

# Sequence Types: list, tuple, range
# List name of my friends
list_friends = []
print(f"list_friends={list_friends} is of {type(list_friends)}")

my_tuple = ()
print(f"my_tuple={my_tuple} is of {type(my_tuple)}")

my_range = range(1)
print(f"my_range={my_range} is of {type(my_range)}")

# Mapping type : dict
my_address = {}
print(f"my_address={my_address} is of {type(my_address)}")