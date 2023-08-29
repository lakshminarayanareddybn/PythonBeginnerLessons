## Practice programs to read the text file "shakespeare.txt"

## Reference
## https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

## 1. Find for a specific keyword given as input by user.
## 2. How many lines are present in the text file
## 3. How many comma's in the text file.
## 4. How many numbers are present in the text file.
## 5. How many vowels are present in the text file.

# version : 1
# file_handle = open("shakespeare.txt", "r")
# file_data = file_handle.read()
# file_handle.close()

# comma_count = file_data.count(",")
# print(f"Number if commans in the file: {comma_count}")

# version : 2
with open("shakespeare.txt", "r") as file_handle:
    file_data = file_handle.read()

    # seek() method makes it possible for you to reset the
    # read/write position in the file.
    file_handle.seek(0)
    file_data_list = file_handle.readlines()
    comma_count = file_data.count(",")

print(f"Number if commans in the file: {comma_count}")
print(f"Number if lines in the file: {len(file_data_list)}")


