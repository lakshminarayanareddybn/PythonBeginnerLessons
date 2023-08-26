### Files can be any file example
## text file .txt
## .json, .bin, .mp3
## functions or operations we can perform on file
## - create
## - read
## - update
## - delete

## File Handling
## the function used to work with any file 
# operations is open() function

## open(filename, mode)
## Takes two parameters: filename, mode

## Different modes for opening file
## "r" - read. default value. Opens a file for reading. error if the file does not exists.
## "a" - append. It opens file for appending. creates the file if it does not exist.
## "w" - write. Open a file for writing. creates the file if it does not exists.
## "x" - creates the specified file, returns an error if file already exists.

## In addition to modes, we can handle file as binary or text mode.
## "t" - Default value. Text mode
## "b" - Binary mode (e.g: images, mp3)

file_handle = open("hello.txt", "r")

# read()
file_data = file_handle.read()
print(type(file_data))
print(file_data)

# readline()
print("Entering while loop")
file_data_1 = file_handle.readline()
while file_data_1 != '':
    print(file_data_1)
    file_data_1 = file_handle.readline()

print("Outside while loop")

# readlines()
file_data_2 = file_handle.readlines()
print(type(file_data_2))
print(file_data_2)

for line in file_data_2:
    print(line)
