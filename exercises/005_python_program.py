## Print all the factors of a given number provided by the user

num = int(input("enter the number > "))

# # 5 : 1,2,3,4,5
for i in range(1, num+1):
    if num%i == 0:
        print(i, end=" ")
