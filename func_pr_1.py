def func1(num1 , num2, num3):
    if(num1>num2):
        gnum=num1
    else:
        gnum =num2
    if(num3>gnum):
        gnum=num3

    return gnum
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
num3 = int(input("Enter a Number: "))
ans = func1(num1,num2,num3)
print(ans)