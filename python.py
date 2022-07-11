# chr() & ord()function:



a=2
print(chr(a))
# return string 

h='A'
print(ord(h))
# return integer

#  String format function()

w='welcome {} To {} cyber Team'.format('Hello',20)

print(w)

x='Hello {} To {} world'.format('welcome','Hacker')
print(x)


# List

b=[1,2,3,4,5,6,7]
print(b,type(b))

print(b[2])

# nested list

j=[10,20,30,40,59,[1,2,3,59]]
print(j)
print(j[4])
print(j[5][1])

# Reverse
k=[10,20,40,60]
print(k[-1: : -1])


# List iteration 
z=[20,30,40,50,60,70]
t=len(z)
for n in range(t):
    print(z[n])


for b in z:
    print(b)


# Reverse
m=[2,3,4,5,6,7,8,9]
r=len(m)

for d in range(r-1,-1,-1):
    print(d)


# List function

# del
# pop()
# remove()
# clear

# del

b=[5,10,20,30,40]
print(b)

del b[1]
print(b)
# delete element for 10

# pop
u=[2,3,4,5]
print(u.pop(2))
print(u)
# pop() delete element for 4

# remove()

k=[10,2,4,5,6]
print(k.remove(6))
print(k)
# remove element for 6

print(k.clear())
print(k)
# clear() list

# insert()
# append()
# extends()

v=[10,20,30,50]
v.insert(0,5)
print(v)
# insert element by 5

v.append(40)
print(v)
# add data front side add element by 40

g=[1,2,3,4]
j=[5,6,7,8]
g.extend(j)
print(g)


 





 










