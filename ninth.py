list_1 = [12, 45, 34, 12, 65, 34]
element_check = int(input("Enter The Element you want to Check: "))
index = 0
c = False

while index<len(list_1):
    if list_1[index] == element_check:
        c = True
        break
    index += 1
if c == True:
    print(f"The Element {element_check} is in the list")
else:
    print(f"The Element {element_check} is not in the list")