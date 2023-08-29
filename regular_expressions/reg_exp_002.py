import re

# findall()
def reg_exp_002_1():
    txt = "The rain is Spain, no body in Pain"
    my_pattern = "ai"

    x = re.findall(pattern=my_pattern, string=txt)
    print(x)
    print(f"The given string has pattern {len(x)} times!!")


def reg_exp_002_2():
    txt = "The rain is Spain, no body in Pain"
    my_pattern = "Portugal"

    x = re.findall(pattern=my_pattern, string=txt)
    print(x)
    print(f"The given string has pattern {len(x)} times!!")

# reg_exp_002_1()
# reg_exp_002_2()