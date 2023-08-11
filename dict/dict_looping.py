# Looping dictionary using for loop

dictionary_1 = {
    "vehicle" : "car",
    "model" : "honda",
    "year" : 2022
}
## print (key, value)s  using for loop
for item in dictionary_1.items():
    a, b = item
    print(f"{a} ==> {b}")

## print values() using for loop
for value in dictionary_1.values():
    print(value)

## print keys() using for loop
for key in dictionary_1.keys():
    print(key)

## print items() using for loop
