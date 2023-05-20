# DUCKTYPING - POLYMORPHISM

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")


# OPERATOR OVERLOADING - POLYMORPHISM
class laptop:

    def code(self,ide):
        ide.execute()

ide=MyEditor() # instead Myeditor can also use Pycharm

lap=laptop()
lap.code(ide)

class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other): # ADDING 2 STUDENTS MARK IN EACH SUBJECT
        m1= self.m1+other.m1
        m2= self.m2+other.m2
        s = student(m1,m2)
        return s

    def __gt__(self, other): # ADDING OR COMPARING 2 STUDENTS MARK
        r1= self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False

    def __str__(self): # ADDING STRINGS AS INT
        return '{}''{}'.format (self.m1,self.m2)


s1=student(54,87)
s2=student(68,54)
s= s1+s2

if s1>s2:
    print("S1 Wins")
else:
    print("S2 Wins")

print(s.m1)
print(s.m2)

print(s1)
print(s2)

# METHOD OVERLOADING
class student:

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a

        return s

s1= student()
print(s1.sum(12,3,5))


# METHOD OVERRIDING
class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")

a=B()
a.show()


# ABSTRACT CLASSES AND METHODS
from abc import *
class comp:
    @ abstractmethod
    def process(self):
        pass

class laptop(comp):
    def process(self):
        print("Running")

class desktop(comp):
    def process(self):
        print("Run")

com=comp()
com.process()

lap=laptop()
lap.process()


desk=desktop()
desk.process()
