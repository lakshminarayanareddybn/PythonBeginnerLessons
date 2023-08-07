## Sorting of list items

## What is sorting?
## Sorting is arranging numbers in ascending or desending order
## when the list items are scrambled

## example : [ 13, 8, 17, 1, 10, 6, 9] # not ordered items
## expected sorted items: [1, 6, 8, 9, 10, 13, 17] # ascending order
## expected sorted items: [17, 13, 10, 9, 8, 6, 1] # decensing order

mylist = [ 13, 8, 17, 1, 10, 6, 9]
print(f" Input list: {mylist}")
mylist.sort()

# sort() method in list. sorts items in ascending order by default
print(f" Sorted list (Ascending): {mylist}")

# How to sort them in descending order?
# sort(reverse=True) will do reverse sorting
mylist2 = [ 13, 8, 17, 1, 10, 6, 9]
mylist2.sort(reverse=True)
print(f" Sorted list (Descending): {mylist2}") #Descending order

## Above methods sort() and sort(reverse=True)  used for sorting.

