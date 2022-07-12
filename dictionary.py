# Dictionary
d={
    'name': 'python',
    'fees': 2000,
    'duration': '2months'

}
print(d)

f=d['fees']
print(f)

for n in d:
    print(d[n])

# Dictionary function

# get()
# keys()
# values()
# items()
# 
dic={

    'name': 'hello',
    'word': 'miss',
    'months': 4

}

# keys()

for n in dic.keys():
    print(n)


# values()

for s in dic.values():
 print(s)


for f,c in dic.items():
    print(f,c)

dic.clear()
print(dic)


dic.update({'word':'love'})
print(dic)

# dict()
# create dictionary

m=dict(name='hello',id='md')
print(m)


# nested dictionary

course={
    'python':{'duration':'2months','fees':'2000',},
    'php':{'duration':'4months','fees':'7000'},
    'java':{'duration':'9moths','fees':'3000'}

}
print(course)

for k,v in course.items():
    print(k,v)
