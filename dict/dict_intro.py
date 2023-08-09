## What is dictionary in python
## <word> : meanings
## dictionaries are used to store key and value pairs
## dictionaries are initialized with {}
## ordered (after 3.7)
## we can modify dictionaries
## dictionaries wont allow duplicates

# ## { key : value }
# simple_example = {"country" : "india"}
# print(type(simple_example))

# print(type(dir(simple_example)))
# methods_in_dict_class = dir(simple_example)
# for method in methods_in_dict_class:
#     if not method.startswith("__"):
#         print(method)

my_dictionary = {
    "name" : "rohan",
    "age" : 20,
    "phone": 12345678,
    "married": False,
    "marks" : [
        30, 40, 50, 50
    ],
    "sibling" : {
        "name" : "sachin",
        "age" : 15
    }
}
# print(my_dictionary)

## access dictionary items
print(f' name: {my_dictionary["name"]}')
print(f' age: {my_dictionary["age"]}')
print(f' sibling: {my_dictionary["sibling"]}')

## add/update the dictionary
## here add means adding new key:value pairs to dictionary
my_dictionary["country"] = "india"
print(my_dictionary)

## update the dictionary item 
my_dictionary["name"] = "nihan"
print(my_dictionary)

dictionary_1 = {
    "vehicle" : "car",
    "model" : "honda",
    "year" : 2022
}

print(dictionary_1)

## len()
## to get length of the dictionary
print(len(dictionary_1))

## dict() method create a new dictionary
dictionary_2 = dict(name="srujan", age=20)
print(type(dictionary_2))

## accessing dictionary item
print(dictionary_2["name"])
print(dictionary_2.get("name"))


