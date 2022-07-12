# Tupple

t= (10,20,30,40)
a=t[2]
print(a)

l=len(t)
for n in range(l):
    print(n)
    print(t[n])


for m in  t:
    print(m)

# Function in Tupple
# min()
# max()
# index()
# sum()
# count()

# min() 
m=(2,3,4,20,30,55,60,50)

print(min(m))
d=min(m)
print(d)
# minimum element by 2


# max()
print(max(m))

j=max(m)
print(j)
# maximum element by 60

# index()

r=m.index(4)
print(r)
# index number fo 4(2)

k=m.count(20)
print(k)


# sum()

x=(10,30,50,60)

s=sum(x,10)
print(s)

# Sets Function

# set()
# add()
# remove()
# clear()
# discard()
# update()
# 

s={10,20,30}
print(s)

for a in s:
    print(a)

m=len(s)
for k in range(m):
 print(k)

# set()

x={10,20,30,40,50,60,70,80,90}
print(x,type(x))
s=set(x)
print(x)

x.add(1)
print(x)
# add element by 1
x.pop()
print(x)
# pop element by 1
x.remove(40)
print(x)
# remove element by 40
x.clear()
print(x)
# clear set retrurn by set() function

l={1,2,3}
q={4,5,6}
l.update(q)
print(l)

q.update(l)
print(q)




