# Inheritance


class A:
    def display(self):
        print("Hello world")
class B():
        def displayB(self):
            print("Hello Hacker")
class C(A,B):

    def displayC(self):
          print("Nice world")

obj=C()
obj.displayC()

# Getter & Setter function

class student:
    def __init__(self):
        self.__name=""
    def getname(self):
            return self.__name
    def setname(self,name):
        self.__name=name


obj=student()
obj.setname("Cyber")
name=obj.getname()
print(name)


