# Question 1: 
# Write a program which will find all such numbers which are divisible by 7 but are not a 
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a 
# comma-separated sequence on a single line.
# Hints: Consider use range(#begin, #end) method


# num = 2002
# # print(num % 7)
# is_num_divisible_by_7 = (num % 7 == 0)
# is_not_multiple_of_5 = (num%5 != 0)
# print(is_num_divisible_by_7)
# print(is_not_multiple_of_5)

# sum = ""
# for num in range(2000, 3201):
#     if num % 7 == 0 and num%5 != 0:
#         sum = sum + f"{str(num)},"

# print(sum)

# 10/7

# 7)14(2
#   14
# -------
#    0

# x = 5//2
# print(x)

# 0  0.5  1

num = input("Enter 3 digit number > ")
print(num[0], int(num[0])**3)
print(num[1], int(num[1])**3)
print(num[2], int(num[2])**3)
sum = int(num[0])**3 + int(num[1])**3 + int(num[2])**3 

if(sum==int(num)):
    print(f"{num} is armstrong number")
else:
    print(f"{num} is not armstrong number")
