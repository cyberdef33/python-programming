# List Comprehersion
a=[]
for n in range(1,101):
    a.append(n)
    print(a)

n=[m for m in range(1,101) if m%2==0]
print(n)


# List Function
# count()
p=[2,5,6,6,6,7,8,2,7,8,9]
n=p.count(6)
print(n)
print(p.count(7))

# max()/maximimum
k=max(p)
print(k)
# maximum value 9

# min()/minimum
k=min(p)
print(k)
# minimum value 2

z=['world','hacker']
j=max(z)
print(j)

# sort()
p.sort()
print(p)

# index()

m=[5,60,30,70]
m.index(5)
print(m)

# iteration two list at a same time 

x=[10,20,30,40,50]
y=[60,70,80,90,99]

for a,b in zip(x,y):
    print(a,b)



# Program to convert string to a list 

n=input("Enter Value:")
a=n.split()
print(a)


x=[]
for a in range(1,4):
    d=input("Enter Value" +str(a)+ ":-")
    print(d)
    x.append(d)
    print(x)
    





