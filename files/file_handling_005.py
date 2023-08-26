## find how many countries are present in the given
## countries.txt file

file_handle = open("countries.txt", "r")
file_data = file_handle.readlines()

print(f"Number of countries in the file {len(file_data)}")

counter = 0
for line in file_data:
    print(len(line))
    if len(line) > 1:
        counter = counter + 1

print(f"Number of countries in the file {counter}")
