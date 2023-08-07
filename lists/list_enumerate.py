## List looping

## Method 1: for loop (discussed last class)
## Method 2: for loop with enumeration

mylist = ["one", "two", "three", "four", "five"]

# Method 1
for item in mylist:
    print(item)

print("=======================\n\n")
for item in enumerate(mylist):
    print(f"i have found \"{item[1]}\" at index \"{item[0]}\"")
    
# enumerate helps us to get the index of item in the list 
# along with the value stiched to it.
