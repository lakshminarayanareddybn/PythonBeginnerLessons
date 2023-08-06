## Stack operations on list
## LIFO: Last In First Out

## Initialize a list
my_books = []

my_books.append("C")      #0 (First)
my_books.append("C++")    #1
my_books.append("Java")   #2
my_books.append("Python") #3 (Last)

print(my_books)
# pop() operation on list. removes the last item
my_books.pop()  # Removes the item at location 3
print(my_books)
my_books.pop()  # Removes the item at location 2
my_books.pop()  # Removes the item at location 1
my_books.pop()  # Removes the item at location 0
print(my_books)

my_books.append("XML")
my_books.append("HTML")
my_books.append("Golang")
my_books.append("Groovy")
print(my_books)

