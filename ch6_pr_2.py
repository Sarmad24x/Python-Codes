print("Enter Your Marks: ")
m1=int(input("1st: "))
m2=int(input("2nd: "))
m3=int(input("3rd: "))
m4=int(input("4th: "))

overall= (m1*m2*m3)/3

if(overall>=40):
    if(m1,m2,m3,m4>=33):
        print("Pass")
else:
    print("Fail")