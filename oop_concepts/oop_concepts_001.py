## Classes/Objects
## 1. Python is object oriented programming language.
## 2. In Python almost everything is an object.
## 3. Object will have its own properites and methods.
## 4. Object is an instance of a class.
## 5. where class is a blueprint for creating objects.

## How to create a class ?
## To create a class use the keyword "class"

## Example
## Create a class named MyClass, with property named x

class MyClass:
    x = 5    

## How to create a object? 
## Since we have MyClass is defined
## Create objects named p1, and print the value of x.

p1 = MyClass()
print(p1.x)

# create another object p2 from MyClass
p2 = MyClass()
p2.x = p2.x + 10
print(p2.x)

# print(dir(p2))

## The __init__() Function
## Above we discussed very simple classes and objects
## But in general it wont be so simple.

## To understand meaning of classed we have to understand
## the builtin function __init__() function.

## All classes have a function called __init__()
## which is always executed when the class is being initiated.

## We use __init__() function to 
## assign values to object properties.


## Example
# Create a class named Person
## use the __init__() function to asssin values for name and age

class Person:
    def __init__(self, name, age, pincode):
        self.name = name
        self.age = age
        self.pincode = pincode

p1 = Person("John", 50, 560048)
# print(dir(p1))
print(p1.age)
print(p1.name)
print(p1.pincode)

## Note:
## The __init__() function is automatically called
## every time the object is created.

## Read and come  for next class
## https://www.geeksforgeeks.org/python-classes-and-objects/
