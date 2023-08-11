my_colors = {
    "green" : 100,
    "red" : 200,
    "blue" : 400
}
print(my_colors)
print(type(my_colors))
print(id(my_colors))

my_colors_copy = my_colors
print(id(my_colors_copy))

my_colors_copy["green"] = 400
print(my_colors)

# copy()

my_colors = {
    "green" : 100,
    "red" : 200,
    "blue" : 400
}
print("+++++++++++++++++++++++++++\n\n")
print(my_colors)
my_colors_copy_1 = my_colors.copy()
my_colors_copy_1["green"] = 400
print(my_colors)

# dict()
my_colors = {
    "green" : 100,
    "red" : 200,
    "blue" : 400
}
print("\n\n--------------------------\n\n")
print(my_colors)
my_colors_copy_2 = dict(my_colors)
my_colors_copy_2["red"] = 600
print(my_colors)
