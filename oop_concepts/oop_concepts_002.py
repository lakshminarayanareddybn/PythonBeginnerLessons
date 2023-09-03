
## create a class called MyCalculator

class MyCalculator:
    
    # class variable are defined inside class
    # class variables are shared for all objects created from the class
    MYCOUNT=0

    def add(self, a, b):
        self.num1 = a
        self.num2 = b
        # print(dir(self))
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def increment(self):
        MyCalculator.MYCOUNT = MyCalculator.MYCOUNT + 1

# Create an instance of MyCalculator
my_calc = MyCalculator()
my_calc1 = MyCalculator()

# Test the methods
result_add = my_calc.add(4, 5)
result_sub = my_calc.sub(40, 5)
result_mul = my_calc.mul(50, 5)
result_div = my_calc.div(60, 5)
print(MyCalculator.MYCOUNT)
my_calc.increment()

# print(result_add)
# print(result_sub)
# print(result_mul)
# print(result_div)

# Test the methods
result_add1 = my_calc1.add(4000, 5)
result_sub1 = my_calc1.sub(40000, 5)
result_mul1 = my_calc1.mul(50000, 5)
result_div1 = my_calc1.div(60000, 5)
my_calc1.increment()

# print(result_add1)
# print(result_sub1)
# print(result_mul1)
# print(result_div1)
print(dir(MyCalculator))
print(MyCalculator.MYCOUNT)
print(dir(my_calc))
