## In python we have two primitive loops
## while
## for

## While loop
## While loop executes as long as the condition is true.

counter = 0
print(counter < 5)
print("Part1: I am entering of while loop")
while counter < 5:
    print(counter)
    counter = counter + 1

print("I am out of while loop")

## break
print("Part2: I am entering of while loop")
counter = 0
while counter < 5:
    if counter == 3:
        break
    print(counter)
    counter = counter + 1

print("I am out of while loop")

## continue
print("Part3: I am entering of while loop")
counter = 0
while counter < 20:
    counter = counter + 1
    if counter % 2 != 0:
        continue
    print(counter)

print("I am out of while loop")
