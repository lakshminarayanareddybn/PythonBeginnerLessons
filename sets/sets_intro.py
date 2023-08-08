## What are sets?

## sets are 
# 1. unorderered
# 2. unchangeable
# 3. unindexed
# 4. duplicates not allowed

# define a sample set
fruits_set = {"apple", "banana", "orange", "banana"}
print(fruits_set)

# # define a list with duplicate values
# mylist = [1,1,1,1,1,1,1,2,3,4,5]
# print(mylist)
# mylist = list(set(mylist))
# print(mylist)

# get length of the set
print(len(fruits_set))

# set can store different data types (strings, tuples, integers, boolean)
mixed_set = {1, "apple", (5,6,7,8), True, False}
print(mixed_set)

print("Boolean values:")
print(True==1)
print(False==0)

## check the type of set
print(type(fruits_set))
