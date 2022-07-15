import random
n=random.randint(2,8)
print(n)
# # randint() return number between 2,8
 n1=random.randrange(2,4)
 print(n1)


 l=[10,20,30,40]
 x=random.choice(l)
 print(x)


r=random.random()
print(r)

p=[10,20,40,50]
random.shuffle(p)
print(p)

u=random.uniform(3,9)
print(u)
