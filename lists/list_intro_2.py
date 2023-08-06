# list allows duplicates

my_list = [1,1,"banana",1,"banana",1,1,1]
# print(my_list)


# List is changeable
# add
# remove
# insert
# extend

# list extend - illustration
list_1 = [20,30,40,50,60]
list_2 = ["banana",20,30,40,50]

## How can i make above list to single list
# extend()
list_1.extend(list_2)
print(list_1)

## How many items i have in my list
total_length = len(list_1)
print(f"Length of list {total_length}")

list_1.pop()
total_length = len(list_1)
print(f"Length of list {total_length}")

## check for type
print(type(list_1))

## Other way of creating list
mylist2 = list((2,3,4,5,6,7)) # [] or list((<>))
print(type(list_1))
print(mylist2[2])


