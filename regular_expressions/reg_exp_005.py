import re

txt = "The rain in Spain"

x = re.findall("[^a-n]", txt)

print(x)