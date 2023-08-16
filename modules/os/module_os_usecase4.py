## Create two folders temp_a, temp_b
## Create a file my.txt inside temp_a
## Move the file from temp_a to temp_b

import os


dir_a = "temp_a"
dir_b = "temp_b"

# create directories

if not os.path.exists(dir_a):
    os.makedirs(dir_a) #temp_a

if not os.path.exists(dir_b):
    os.makedirs(dir_b) #temp_b

file_name = "my.txt"
full_path = os.path.join(os.getcwd(), dir_a, file_name)

if not os.path.isfile(full_path):
    with open(full_path, "w") as tmp_file:
        pass

new_full_path = os.path.join(os.getcwd(), dir_b, file_name)
os.rename(full_path, new_full_path)
