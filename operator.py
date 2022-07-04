# Operator in python
# Arithmetic operator

a=50
b=60
print("a+b") 
print(a+b) 
print(a-b) 
print(a*b) 
print(a/b) 

# Assignment operator

print(a==b)
print(a<b)
print(b>a)

# Comparison operator

print(a!=b)
print(a==b)
print(b!=a)
print(b>=a)


# Logical operator
#  and operator: or operator: not operator

print(a==50 and a<b)
print(b!=a or a<=b )
print(a!=50 or a<b or a==b)
print(not a!=50)


# Membership operator
# In & Not in operator

var="Hello world"      
print('h'in var)
print('w'in var)
print('z'not in var)

# Example
a=[10,20,40,50,70]
print(20 in a)
print(100  in a)

# Bitiwise operator
# & operator
# | operator
# ^ xor operator
x=10
y=20
print(bin(x))
# 10=1010
print(bin(y))
# 20=10100
print(bin(x&y),x&y)
# output x&y=0 0
print(bin(x|y),x|y)
# output x|y= 11110 30
print(bin(x^y),x^y)
# output x^y=11110 30





