## Create a directory and files inside it

import os

# create a temp folder in current working directory
tmp_dir_name = "temp_dir"

if os.path.exists(tmp_dir_name):
    print(f"Directory {tmp_dir_name} already exists. Hence skipping directory creation!!")
else:
    print(f"Creating Directory {tmp_dir_name}")
    os.makedirs(tmp_dir_name)

full_path = os.path.abspath(tmp_dir_name)
print(full_path)

list_of_files = [
    "banana.txt",
    "orange.txt",
    "apple.txt"
]

for file in list_of_files:
    # /workspaces/PythonBeginnerLessons/modules/temp_dir + banana.txt
    file_path = os.path.join(full_path, file)
    print(file_path)
    with open(file_path, "w") as empty_file:
        pass

