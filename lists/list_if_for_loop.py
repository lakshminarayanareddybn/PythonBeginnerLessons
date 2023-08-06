## if loops are used to check for logical conditions
## that should resulted into true or false

## equals :  var1 == var2 
## not equals :  var1 != var2 
## less than : var1 < var2
#  less than or equal to: var1 <= var2
## greater than : var1 > var2 
#  greater than or equal to: var1 >= var2

## Nested if-elses are possible in python

fruits = ["banana", "orange", "apple", "guava"]

for item in fruits:

    # equals
    if item == "banana":
        print("Hello banana")
    else:
        # not equals
        if item != "orange":
            print(f"Not interested {item}")
        else:
            print("Hello orange we got you!!")

age_group = [20, 30, 40, 50, 60]

for age in age_group:
    
    # print ages which are less than 30
    # less than
    if age < 30:
        print(age)

    # less than or equal to
    if age <= 30:
        print(age)
    
    # print age greater than 30
    if age > 30:
        print(age)

    # print ages greater than or equal to 30
    if age >= 30:
        print(age)

    if age > 30 and age <50:
        print(age)


## check if list has item using if condition

if 70 in age_group:
    print("Hey item is available")
else:
    print("Not available")


for item in age_group:
    if item == 30:
        print("Hey item is available")
        

## if-elif-else
a = 3300
b = 3300

if b > a:
    print("b is greater than a")
elif a==b:
    print(" a and b are equal")
else:
    print("a is greather than b")
