## Convert Decimal number to octal using print() output formatting
number = int(input("Enter the decimal number > "))
print(f"Decimal number entered: {number}")

oct_number = oct(number)
print(f"Octat number is: {oct_number[-2:]}")
