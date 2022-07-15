# class Example:
#     a=10
#     def showvalue(self):
#         print(self.a)
#         self.c=self.a*self.a
#         print(self.c)
# obj=Example()
# obj.showvalue()

# Inheritance

class A:
    def DisplayA(self):
        print("Welcome To Cyber Team:")
class B(A):
    def DisplayB(self):
        print("Welcome To World:")
# obj=A()
# obj.DisplayA()
obj=B()
obj.DisplayB()
obj.DisplayA()


