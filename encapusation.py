class student:
    __name="Ravi"
    def __init__(self):
        print(self.__name)
        self.__display()
    def __display(self):
        print("welcome cyber world")

obj=student()
# obj.__display()

#  Polymorphism 

l=[10,20,30,50]
print(len(l))
s='hacker'
print(len(s))

# function overlodading & overiding


# class Name:
#     def display(self,name=''):
#         print("welcome to cyber "+name)


# obj=Name()
# obj.display()
# obj.display('security')

# Overriding

class Cyber:
    def display(self):

        print("Cyber ")

class Tech(Cyber):


    def display(self):

        print("Nice world")
obj=Tech()
obj.display()


#  Overloading

class Area:
    def find_area(self,x=None,y=None):

        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("Nothing")
obj=Area()
obj.find_area()
obj.find_area(10)
obj.find_area(4,5)
