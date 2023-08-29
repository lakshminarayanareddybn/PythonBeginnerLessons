# split() function
# it returns a list where the string has been split at each match

import re

def reg_exp_005_1():
    txt = "The rain is Spain"
    my_pattern = "\s"
    result = re.split(my_pattern, txt)
    print(result)
    print(f"Number of words in the given sentence is {len(result)}")

def reg_exp_005_2():
    with open("../files/shakespeare.txt", encoding="utf-8") as fh:
        data = fh.read()

    my_pattern = "\s"
    result = re.split(my_pattern, data)
    print(f"Number of words in the given sentence is {len(result)}")

    my_pattern2 = "\d{2}"
    x = re.finditer(pattern=my_pattern2, string=data)
    
    if x is not None:
        print(f"Number of two digit occurrences in the given text data is {len([ item for item in x])}")
        # for item in x:
        #     print(item.group())

def reg_exp_005_3():
    with open("../files/shakespeare.txt", encoding="utf-8") as fh:
        data = fh.read()

    my_pattern2 = "CLEOPATRA"
    x = re.finditer(pattern=my_pattern2, string=data, flags=re.I)

    if x is not None:
        print(f"Number of two digit occurrences in the given text data is {len([ item for item in x])}")

# reg_exp_005_1()
# reg_exp_005_2()
reg_exp_005_3()
