import os
import pathlib

items = os.listdir("/workspaces/PythonBeginnerLessons/modules")
# print(type(items))

# Iterate through the items
for item in items:

    # to get the full path or absolute path "os.path.abspath"
    full_path = os.path.abspath(item)

    # to filter ".txt" files alone use "in" keyword
    if ".txt" in full_path or ".py" in full_path:
        
        # open the text file and print the contents 
        # open()
        with open(full_path) as in_file:
            txt_data = in_file.read()
            print(txt_data)

    else:
        print(f"Skipping file {full_path}")
