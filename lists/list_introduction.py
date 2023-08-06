## List can be collection of things/items
## which are enclosed in []
## and seperated by comma

## Lists are sequence data types

## Other sequence data types are Tuples, String

str = "hello"
print(str[0], str[-5])

str2 = "abrakadabra"
print(str2[::3])

str3 = "telugu"
print(str3[::-1])

# Add element to list
initial_list = [100,200,400,500,600,800]
print(f"Initial list: {initial_list}")
initial_list.append(900)
print(f"After appending 900 to list: {initial_list}")

# Insert missing numbers 300 and 700 to the "initial_list" list
initial_list.insert(2,300)
print(f"After inserting element 300 at index 2: {initial_list}")
initial_list.insert(6,700)
print(f"After inserting element 700 at index 6: {initial_list}")

## After updating the list we got [100, 200, 300, 400, 500, 600, 700, 800, 900]
## Remove items from the list
del initial_list[0]
print(f"After deleting/removing element 100 at index 0: {initial_list}")

initial_list.remove(500)
print(f"After deleting/removing element 500 : {initial_list}")

