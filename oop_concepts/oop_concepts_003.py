
## create a class called MyCalculator

class MyCalculator2:

    def __init__(self, a, b):
        # Instance variables are initialized after creating object
        # Every object will have its own copy of instance variables.
        # Always define or initialize instance variables inside __init__ function.
        # __init__ function is special method, which always gets called whenever we create an object.

        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2
    
    def div(self):
        if self.num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return self.num1 / self.num2


# Create an instance of MyCalculator
my_calc = MyCalculator2(4000, 5)

# Test the methods
result_add = my_calc.add()
result_sub = my_calc.sub()
result_mul = my_calc.mul()
result_div = my_calc.div()

print(result_add)
print(result_sub)
print(result_mul)
print(result_div)