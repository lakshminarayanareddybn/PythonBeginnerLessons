MY_COUNT = 0

def add(num1, num2):
    global MY_COUNT
    MY_COUNT += 1
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def div(num1, num2):
    return num1 / num2

def mul(num1, num2):
    return num1 * num2
