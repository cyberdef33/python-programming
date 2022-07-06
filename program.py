# How to take input form user

a= int (input("Enter Number"))
print(a)

x= int (input("Enter your 1st Number:"))
y= float (input("Enter your 2nd Number:"))
print(x+y)



# Condition statement
# if statement
# if else statement
# if elef else statement


result= int (input("Enter Number:"))
if result==5:
    print('Result',type(result))

elif result==10:
    print(result)

else:
    print('Invalid Operation')


# Calculator

print('''
       +Add
       -Substract
       * Multiplication
       / Division 
 ''')
x=int (input("Enter 1st Number:"))
y=int (input("Enter 2nd Number:"))

opr=input("Enter operator")
if opr=='*':
 print(x*y)
elif opr=='+':
 print(x+y)
elif opr=='-':
 print(x-y)
elif opr=='/':
 print(x/y)
else:
 print('Invalid operation')

