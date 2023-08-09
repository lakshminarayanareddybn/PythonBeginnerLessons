myset = {"apple", "banana", "orange"}

## How can i acccess element in sets
#print(myset[0]) # we cant use index for accessing sets element

for item in myset:
    print(item)

## How check element is present in sets
if "banana1" in myset:
    print("Found banana")
else:
    print("Not found")

## add()
myset.add("apple1")
print(myset)

# Update myset1 with myset2.
# extending sets or merging sets
myset2 = {"blue", "red", "green"}

## update()
myset.update(myset2)
print(myset)

## remove()
## Remove items from sets
myset.remove("red")
print(myset)

# discard()
myset.discard("blue")
print(myset)

## myset = {'apple', 'banana', 'orange', 'apple1', 'green'}
## pop()
myset.pop()
print(myset)

## clear()
myset.clear()
print(myset)


## del
# myset3 = {"blue", "red", "green"}
# del myset3
# print(myset3)

# mylist = ["blue", "red", "green"]
# del mylist[0]
# print(mylist)

## Joining the sets using union()
set_a = {"red", "blue", "green"}
set_b = {4, 5, 6}
set_c = set_a.union(set_b)
print(set_c)
