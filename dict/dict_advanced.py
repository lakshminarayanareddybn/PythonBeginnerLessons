
dictionary_1 = {
    "vehicle" : "car",
    "model" : "honda",
    "year" : 2022
}

# How many keys are in my dictionary
# and what are they?
# keys()
dictionary_1_keys = list(dictionary_1.keys())
print(dictionary_1_keys)

# len() on keys()
print(len(dictionary_1_keys))

# values()
print(list(dictionary_1.values()))

## we discussed so far to get either key or values
## how about getting both together.
## items()
print(dictionary_1.items())

for key, value in dictionary_1.items():
    print(key, value)

# how to check if item is present in the dictionary or not
if "model" in dictionary_1:
    print("found model in dictionary")
else:
    print("not found")
