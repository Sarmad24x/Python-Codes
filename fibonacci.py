def fibo(n):
    if (n<=1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
inpu = int(input("Enter: "))
fibo(inpu)
for i in range(inpu):
    print(fibo(inpu))