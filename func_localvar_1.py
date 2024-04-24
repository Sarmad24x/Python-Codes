#This Program is used to explin the the use of local variables

def num(x):
    print("X is ",x," here.")
    x = 2
    print("Now the value is changed into ",x)

x = 50
num(x)
print ("Here x is ",x)