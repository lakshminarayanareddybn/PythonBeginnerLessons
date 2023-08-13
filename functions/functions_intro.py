## what is a function in python?
## function is a block of code/statements which
## executes or runs only when we call it.

# def function_name(parameters):
#     # statement 1
#     # statement 2
#     # statement can be an assignment, or
#     # checking of if, for, while
#     # list, tuple
#     return expression

# #function_name()

## we can pass data to the functions , we call it as
## parameters into a function

## functions can return data. which generally we call
## as results

## How to define a function in python?
## in python we use "def" keyword to define a function.

# define a function "hello"
# def hello1():
#     print("hello world 2!!")
#     print("hello world 2!!")

# def hello2():
#     print("hello world 2!!")

# ## make call to function
# hello1()
# hello2()

## Benefits of using functions
# - Increase the code readibility
# - Increase the code reusability

## There are two types functions in python
## 1. Builtin library functions
##### - These generally are from python standard functions.
## 2. User-defined functions
##### - We can create our own functions based on our requirements.

## Create a function 
## To create a function in python, we use "def" keyword.


## 1. define a simple function
def fun():
    print("Hello Shyam")

## 2. Calling a python function
## we make call to function using function name followed
## by parenthesis containing parameters of the function.
fun()

## Python functions with parameter and return time
def add(num1:int, num2:int) -> int:
    """
    Add two numbers and return the sum value
    """
    sum = num1 + num2
    return sum


result = add(10, 8)
print(f"result: {result}")

result = add(11000, 118)
print(f"result: {result}")

result = add(3000, 20)
print(f"result: {result}")

result = add(45, 10)
print(f"result: {result}")
