# Modify strings
# In python we have many builtin methods that we can use with strings

# # CTRL+/ : Comment or uncomment the python code
# ## Convert a given string to Upper case
# input_string = "hello bangalore"

# # print(dir(str))

# print(f"Original string: {input_string}")
# print(f"Modified string: {input_string.upper()}")


# # Convert string to lower
# onemore_string = "HJAFHFAFHFDAHGFHGDF"
# print(f"Original string: {onemore_string}")
# print(f"Modified string: {onemore_string.lower()}")

# ## Strip
# ## Remove  white space before and/or after the actual text or string.

# str_with_space = "     Hello                      Bangalore   "
# print(str_with_space)
# print(str_with_space.strip())

# ## Replace
# input_string = "Hello Bangalore. How are you today?"
# print(input_string)

# replaced_string = input_string.replace("Bangalore", "Hyderabad")
# print(replaced_string)

## Split
## It splits the string based on the seperator and returns the list of strings.

input_string_with_commas = "Hello, world"
print(input_string_with_commas.split(","))

