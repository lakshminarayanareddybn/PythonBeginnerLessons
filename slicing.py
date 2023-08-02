## Strings: Slicing
## We can get range of characters using slicing feature python
#                        543210
hello_blore = "Hello, Bangalore"
#              0123456789

print(hello_blore[0]) # H
print(hello_blore[1]) # e
print(hello_blore[9]) # 9

make_word = hello_blore[0]+hello_blore[1]+ ' '+ hello_blore[9]
print(make_word)

# get slice from index 7 to 11
print(hello_blore[7:12])


# Slice from the start
print(hello_blore[:5])
print(hello_blore[2:])

# start: end

# Slice from the end
print(hello_blore[-5:-2])