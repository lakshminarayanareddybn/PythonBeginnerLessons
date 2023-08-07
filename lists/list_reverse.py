## Reverse the list
my_list = [9,5,2,99,12,88,34]

# Approach#1
my_list.reverse()
print(my_list)

# here reverse() function just reversed the list without sorting.

my_list2 = [88,65,33,21,11,98]
# Approach#2
print(my_list2[::-1])

# sorted() method takes list as input. sorts the list and returns new list
# without modifying the actual list provided as input.
print(sorted([88,65,33,21,11,98]))


fruits = ["banana", "orange", "apple", "guava", "banana"]

# check how many times "banana" is present in my fruits list
print(f"banana count in fruit list is  {fruits.count('banana')}")

# count() method provided with class list. will give us count
print(f'orange count in fruit list is  {fruits.count("orange")}')

