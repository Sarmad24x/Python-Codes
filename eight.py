
my_list = [2, 5, 6, 67, 53, 32]
largest_element = my_list[0]

for element in my_list:
    if element > largest_element:
        largest_element = element

print("The largest element in the list is:", largest_element)
