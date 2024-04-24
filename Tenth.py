def running_total(input_list):
    total = 0
    running_totals = []

    for num in input_list:
        total += num
        running_totals.append(total)

    return running_totals

# Example of using the function
my_list = [1, 2, 3, 4, 5]
result = running_total(my_list)
print("Running total of the list:", result)
