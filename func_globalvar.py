def func():
    global x
    print("X is ",x)
    x = 2
    print("x is now: ",x)
x =50
func()
print ("Value of x",x)   