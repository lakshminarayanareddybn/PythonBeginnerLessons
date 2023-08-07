## How to join lists
## We have provided with more than one list.
## We would like to combine them

# Define two lists
list1 = ["one", "two", "three", "four"]
list2 = ["five", "six", "seven", "eight"]

print(list1)
print(list2)

# First approach: using "+" (plus) operator
list3 = list1 + list2

print(f"Joined list with approach#1: {list3}") # merged list

# Second approach: using extend() method
list1.extend(list2)

print(f"Joined list with approach#2: {list1}") 
