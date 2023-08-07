## Copy list 
## Why do we need to copy list?
## Sometimes we want to keep original list as is and work on the copy.

mylist = ["one", "two", "three", "four", "five"]
print(mylist) #output: ['one', 'two', 'three', 'four', 'five']

# Create a new  reference "mylist1"
mylist1 = mylist

# print mylist1
print(mylist1) #output: ['one', 'two', 'three', 'four', 'five']

### both mylist and mylist1 have same data

print(id(mylist)) # Memory location: 140626113912384
print(id(mylist1)) # Memory location: 140626113912384

## so when we assigned 
## mylist1 = mylist
## it created a reference to same memory location

# try modifying the mylist1
mylist1.append("six")

## try printing mylist
print(mylist)

# Since mylist1 is only reference to mylist. changing
# mylist1 also impacts mylist

# Now how to create seperate copy of mylist. but not reference as above
# copy() creates seperate copy of mylist and returns.
mylist_copy = mylist.copy()

## check the memory locations of mylist and mylist_copy
print(id(mylist_copy)) # Memory location: 140216110320448
print(id(mylist)) # Memory location: 140216113495680

# So we have different copies now
print(mylist_copy)
print(mylist)

# Now try modifying mylist_copy
mylist_copy.append("seven")

print(mylist_copy) # This has extra "seven" now
print(mylist)







