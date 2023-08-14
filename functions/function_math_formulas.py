# define a function to calculate area of square
# area of square = a*a

def area_of_square(a):
    result = a*a
    return result

# print(f"Area of square is {area_of_square(40)}")

def are_of_circle(radius):
    result = 3.14*(radius**2)
    return result

# print(f"Area of cicle: {are_of_circle(4.5)}")

def sum_all_nums(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return sum

result1 = sum_all_nums(2,3)
# print(f"Result is {result1}")

result2 = sum_all_nums(2,3,4,5,6,7,8,9,10)
# print(f"Result is {result2}")

def set_address(country=None, pincode=None, name=None):
    print(f"country : {country}")
    print(f"pincode : {pincode}")
    print(f"name: {name}")

set_address(country="india", pincode=560001, name="Johan")

## **kwargs
def set_address2(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

set_address2(country="USA", pincode=3456676, name="Alex", age=20)

## Passing list to function
list_var = [2, 3, 4, 5, 10000]

def sum_my_list(input_list):
    sum = 0
    for item in input_list:
        sum = sum + item
    return sum

result = sum_my_list(list_var)
print("******************************\n\n")
print(result)

