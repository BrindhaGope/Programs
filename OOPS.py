# TO PRINT USING CLASS
class comp:

    def config(self):
        print('i5','16GB','1TB')

com1=comp()
com2=comp()

comp.config(com1)
com2.config()

# TO PRINT USING __INIT__
class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram


    def config(self):
        print("Config is:",self.cpu,self.ram)


com1=computer('i5','16')
com2=computer('Ryzen3','8')

com1.config()
com2.config()

#TO COMPARE THE ARGUMENTS
class comp:
    def __init__(self):
        self.name='Navin'
        self.age=28

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=comp()
c1.age=30
c2=comp()

if c1.compare(c2):
    print("Same")
else:
    print("Different")


print(c1.name,c1.age)
print(c2.name,c2.age)


# CONSTRUCTOR
class comp:
    def __init__(self):
        self.name = 'Navin'
        self.age = 28


c1 = comp()
c2 = comp()

print(c1.name, c1.age)
print(c2.name, c2.age)

# TO UPDATE OR SELF
class comp:
    def __init__(self):
        self.name='Navin'
        self.age=28

    def update(self):
        self.age=30

c1=comp()
c1.update()
c2=comp()

c2.name="Rashi"
c2. age=12

print(c1.name,c1.age)
print(c2.name,c2.age)

# TO UPDATE CLASS VARIABLE
class car:
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()
c1.mil=8
car.wheels=5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)


# PRINT TYPES OF METHODS
class stud:
    school='Telusko'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("Student class")

s1=stud(34,47,32)
s2=stud(89,32,12)

print(s1.avg())
print(stud.getschool())
stud.info()


# INNER CLASS

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand="HP"
            self.ram=16

        def show(self):
            print(self.brand,self.ram)


s1=student("Navin",2)
s2=student("Jenny",3)

s1.show()
s2.show()

lap1=s1.lap
lap2=student.laptop()

print(id(lap1))
print(id(lap2))


# INHERITANCE AND CONSTUCTOR IN INHERTIANCE AND MRO
class A:

    def   __init__(self):
        print("A init")

    def feature1(self):
        print("1 is working")

    def feature2(self):
        print("2 is working")
class B:

    def __init__(self):
        print("B init")

    def feature1(self):
        print("3 is working")

    def feature4(self):
        print("4 is working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C init")

    def feat(self):
        super().feature2()



a1=C()
a1.feat()

