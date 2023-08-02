## Format Strings

## I have a string and a number. How can i combine it

# my_name = "I am X person. with age "
# my_age = 20

# about_me = my_name + my_age
# print(about_me)

# ### TypeError: can only concatenate str (not "int") to str

# ## To combine strings and numbers we need to use
# # format() or {} inside the print

# about_me = "{} {}".format(my_name,my_age)
# print(about_me)

# about_me = f"{my_name} {my_age}"
# print(about_me)

# print(f"{my_name} {my_age}")
# print("{} {}".format(my_name,my_age))


user_name = input("Enter your name > ")
user_age = input("Enter your age > ")

welcome_template = "Hello {}. Your age recorded will be {}"
print(welcome_template.format(user_name, user_age))