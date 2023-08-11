# Remove dictionary items
student = {
    "name" : "suhan",
    "age" : 17,
    "school" : "Baldwin"
}
print(student)

# pop()
print(f'{student.pop("age")} is removed')
print(student)

# popitem()
student.popitem()
print(student)

# del
del student["name"]
print(student)

# clear()
student = {
    "name" : "suhan",
    "age" : 17,
    "school" : "Baldwin"
}
print(student)
student.clear()
print(student)
