print("Enter Your Marks: ")
m1=int(input("Physics: "))
m2=int(input("Maths: "))
m3=int(input("Chemistry: "))
m4=int(input("Computer: "))
m5=int(input("Urdu: "))
m6=int(input("Biology: "))

avg=(m1+m2+m3+m4+m5+m6)/6

if (avg>=90):
    print("A+")
elif(avg>=80 and avg<90):
    print("A")
elif(avg>=70 and avg<80):
    print("B")
elif(avg>=60 and avg<70):
    print("C")
elif(avg>=50 and avg<60):
    print("B")
else:
    print("Fail")
    