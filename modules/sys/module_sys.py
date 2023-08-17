import sys

print(dir(sys))
print(sys.path)

# sys module provides control over input or output
# it allows us to redirect the input and output to any other devices

# Read about below variables
# stdin
# stdout
# stderr

# stdin: 
# - It can be used to get input from the command line directly.
# - it can be used as standard input.
# - it internally uses input() input.
# - it adds "\n" at the end of each sentence.

for name in sys.stdin:
    print(f"Your input was {name}")

name = input("Enter your input: > ")
print(name.upper())


# stdout
# it is used to display the output directly to screen console

sys.stdout.write("Hello ")

# stderr
# whenever if there is any error inside python it will be written sys.stderr

def write_to_strerr(*a):
    print(*a, file=sys.stderr)

write_to_strerr("Hey whatsup")
