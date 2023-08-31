# sub() function
# it comes as part of re module

# sub() replaces the matches with the test of our choice

import re

txt = "The rain in Spain"

x = re.sub("[a-n]", "-", txt)
# print(x)

y = re.sub("[a-n]", "-", txt, count=2)
# print(y)

## Match Object
## It is an object contains information about search and the result
## If there is no match, the value None will be returned instead match object

z = re.search("ai", txt)
# print(z.group())

z = re.finditer("ai", txt)

for item in z:
    print("++++++++++++++\n\n")
    print(item.span())
    print(item.group())
    print(item.start())
    print(item.end())

z = re.findall("ai", txt)
# print(z)
