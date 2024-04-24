num = 23
guess = int(input("Enter an Integer: "))
if guess == num:
    print("You guessed it!!!")
elif guess < num:
    print("A bit Higher.")
else:
    print("A bit Lower.")
print("Done")    