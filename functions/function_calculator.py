## Exersize
## Define below functions and call them with sample values
## subract(num1: int, num2:int) -->int - subract num2 from num1 and return the result.
## multiply(num1: int, num2:int) -->int - multiply num1 and num2. then return the result.
## divide(num1: int, num2:int) -->int - divide num1 by num2. then return the result.

# mynum = 40

# def my_func():
#     mynum = 20
#     print(f"mynum in my_func(): {mynum}")
#     return mynum

# mynum = my_func()
# print(f"mynum value is {mynum}")

# def subract(num1: int, num2:int)
def subract(num1, num2):
    result = num1 - num2
    return result

print(subract(4,3))

def multiply(num1, num2):
    result = num1 * num2
    return result

print(multiply(4,3))

def greet():
    print("Hello how are you?")
    
greet()