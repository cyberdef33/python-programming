import random
cnumber=random.randrange(1,101)
userInput=int(input("Enter Your Number:"))
if userInput>cnumber:
    print("Computer Number",cnumber)
    print("Your Number is High")
elif cnumber>userInput:
    print("Computer Number",cnumber)
    print("Your Number is Low")
else:
    print("Computer Number",cnumber)
    print("Your Number is equal")
