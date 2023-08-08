
colors = ("red", "blue", "green")

# We can extract values back to variables. it is terms as "unpacking"
myvar1, myvar2, myvar3 = colors

print(f"myvar1: {myvar1}")
print(f"myvar2: {myvar2}")
print(f"myvar3: {myvar3}")

# Asterisk (*)
colors2 = ("red", "blue", "green", "yellow", "orange", "cyan")
myvar1, myvar2, *myvar3 = colors2

print(f"myvar1: {myvar1}")
print(f"myvar2: {myvar2}")
print(f"myvar3: {myvar3}")

myvar1, *myvar2, myvar3 = colors2

print(f"myvar1: {myvar1}")
print(f"myvar2: {myvar2}")
print(f"myvar3: {myvar3}")

## Loop through tuples
print("Loop example: ")
for item in colors2:
    print(item)

## Loop through index
print("Loop example with indexing: ")
for item in range(len(colors2)):
    print(colors2[item])

## While loop
colors3 = ("red", "blue", "green", "yellow", "orange", "cyan")
index = 0
while index < len(colors3):
    print(colors3[index])
    index = index+1
    
## Multiply tuples
print(colors3 * 10)

## tuple has only two methods
## count(), index()

