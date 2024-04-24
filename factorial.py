n = int(input("Enter an Integer: "))
if n == 0:
    print("1")
elif n == abs(n):
    fact = 1
    for i in range (1,n+1):
        fact = fact*i
    print (fact)
else:
    print('error')