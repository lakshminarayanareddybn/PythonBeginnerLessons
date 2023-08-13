## Define a function to check is the given
## input paramater is prime or not.
## if prime returns True else return False.

## What is prime number?
## Prime numbers are greater than 1
## Prime numbers divisble by 1 and the number itself
## Example: 3 is prime, 3 is divisible 1 and 3 only.

def is_prime(num: int) -> bool:
    result = False
    if num > 1:
        ## Add your logic to check if `num` is prime or not
        for value in range(2, num):
            if(num % value) == 0:
                result = False
                break
        else:
            result = True
    else: 
        result = False
    return result

# while True:
#     input_value = int(input("Enter number: > "))
#     if is_prime(input_value) == True:
#         print(f"{input_value} is prime")
#     else:
#         print(f"{input_value} is not prime")


### Built-in functions
list_a = [1,12,3,4,5]

print(len(list_a))

float_value = 4.678
print(abs(float_value))

print(max(list_a))

tuple_b = (10, 12, 13)
print(max(tuple_b))

print("Hey {}".format(tuple_b))

print(min(tuple_b))


## Exersize
## Define below functions and call them with sample values
## subract(num1: int, num2:int) -->int - subract num2 from num1 and return the result.
## multiply(num1: int, num2:int) -->int - multiply num1 and num2. then return the result.
## divide(num1: int, num2:int) -->int - divide num1 by num2. then return the result.
