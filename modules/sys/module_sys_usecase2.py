import sys

print(sys.path)

print(sys.modules)

print(sys.maxsize)

def myfunc():
    print("hello")

print(sys.settrace(myfunc))