## Accept any three string/words from one input() call

input_string = input("Input three word string > ")
print(input_string)

split_input_string = input_string.split("+")
print(type(split_input_string))
print(split_input_string)
print(split_input_string[0])
print(split_input_string[1])
print(split_input_string[2])