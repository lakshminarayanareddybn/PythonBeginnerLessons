# When defining a string variable, if string contains
# any illegal character, python intepreter throws compile error.

# Hello world, "how are you"
escape_sample = "Hello world, \" how are you\" "
print(escape_sample)

# \ is called escaping character

single_quote_sample = 'Hello world, \' how are you\' '
print(single_quote_sample)

# \\ - Backslash
# \n - New Line
# \r - Carriage Return
# \t - Tab
# \b - Backspace
# \f - Form feed (Try)
# \ooo - Octal value (Try)
# \xhh - Hex value (Try)

slash_sample = "Print backslash \\"
print(slash_sample)

newline_sample = "My \\n new \\n line"
print(newline_sample)

tab_sample = "My \\t tab \\t sample"
print(tab_sample)
