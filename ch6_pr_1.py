print("Enter 4 Numbers:\n")
num1=int(input("1st: "))
num2=int(input("2nd: "))
num3=int(input("3rd: "))
num4=int(input("4th: "))
if(num1>num2):
    maxnum = num1
else:
    maxnum = num2
if (num3>num4):
    maxnum2=num3
else:
    maxnum2 =num4
if maxnum>maxnum2:
    ans = maxnum
else:
    ans=maxnum2

print(ans)