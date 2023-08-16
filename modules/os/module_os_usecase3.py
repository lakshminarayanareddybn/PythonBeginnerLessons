import os
import time

## Delete files and the directory "temp_dir"
dir_name = "temp_dir"

dir_items = os.listdir(dir_name)
print(dir_items)

for item in dir_items:
    full_path = os.path.join(os.getcwd(), dir_name, item)
    print(f"Deleting file {full_path}")
    os.remove(full_path)
    time.sleep(5)

print("Finally removing directory...")
os.removedirs(dir_name)
