## Format variables using a string.format() method
## Write a program to use string.format() method to format the
## below three variables as per the expected output

totalMoney = 1000
quantity = 3
price = 450

## expected output is:
## I have 1000 dollars so i can buy 3 football for 450.00 dollars.

print("I have {} dollars so i can buy {} football for {:.2f} dollars".format(totalMoney, quantity, float(price)))
print(f"I have {totalMoney} dollars so i can buy {quantity} football for {price:.2f} dollars")
