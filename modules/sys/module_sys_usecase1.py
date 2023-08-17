import sys

## Command line arguments
## - we pass Command line arguments  during the calling of the program.

## python module_sys_usecase1.py 3 4
print(type(sys.argv))

print(sys.argv)

if len(sys.argv) > 1:
    num1 = sys.argv[1]
    num2 = sys.argv[2]
    
    if sys.argv[3] == 'add':
        total = int(num1) + int(num2)
        print(f"add total: {total}")
else:
    sys.exit("Usage: python module_sys_usecase1.py 3 4 sum")

print("Hello is it coming here")
