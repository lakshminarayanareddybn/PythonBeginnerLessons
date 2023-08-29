# search() : searches the string for a match and returns
# the match object if there is a match,
# otherwise it returns None

import re

def reg_exp_003_1():
    txt = "The rain is Spain"
    my_pattern = "\s"

    x = re.search(pattern=my_pattern, string=txt)
    if x is not None:
        print(x.start(), x.end())

def reg_exp_003_2():
    txt = "The rain is Spain"
    my_pattern = "\d"

    x = re.search(pattern=my_pattern, string=txt)
    if x is not None:
        print(x.start(), x.end())
    else:
        print("Pattern not found in the string!!")

def reg_exp_003_3():
    txt = "The rain is Spain with temp 45"
    my_pattern = "\d{2}"

    x = re.search(pattern=my_pattern, string=txt)
    if x is not None:
        # print(x.start(), x.end())
        print(x.group())
    else:
        print("Pattern not found in the string!!")

def reg_exp_003_4():
    txt = "My age is 20. and my mobile number is 9009090090"
    my_pattern = "\d{10}"

    x = re.search(pattern=my_pattern, string=txt)
    if x is not None:
        # print(x.start(), x.end())
        print(x.group())
    else:
        print("Pattern not found in the string!!")

def reg_exp_003_5():
    txt = "My age is 20. and my mobile number is 9009090090. My room number is 12."
    my_pattern = "\s\d{2}\."

    x = re.finditer(pattern=my_pattern, string=txt)

    for item in x:
        print(item.group())

# reg_exp_003_1()
# reg_exp_003_2()
# reg_exp_003_3()
# reg_exp_003_4()s
reg_exp_003_5()