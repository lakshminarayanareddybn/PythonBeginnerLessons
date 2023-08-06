# Take two numbers as input from user
# and add/sum them and print to terminal

# Take first number as input from user
num1 = input("Input number 1 > ")

# Take second number as input from user
num2 = input("Input number 2 > ")

print(f"num1 entered by user {num1}")
print(f"num2 entered by user {num2}")

# Add/sum num1 and num2
# Casting : type cast from string to integer and then perform sum
# '+' - addition
sum = int(num1) + int(num2)

# Print the sum/total value to terminal
print(f"Sum is {sum}")


sub = int(num1) - int(num2)

# Print the Subtraction value to terminal
print(f"Sub is {sub}")