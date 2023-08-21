## Accept a list of 5 float number as an input from the user

float_num_list = []

counter = 0
while counter < 5:
    print(counter)
    num = float(input("Enter the float number > "))
    float_num_list.append(num)
    counter = counter + 1


print(float_num_list)
    
