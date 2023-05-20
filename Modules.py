def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b


# TO IMPORT FROM ONE FILE TO ANOTHER
from Modules import *
a,b=5,5
c=add(a,b)
print(c)


# PRINT USING DEF MAIN FUNC
def fun1():
    print("Hello")
def fun2():
    print("Welcome")
def main():

    fun1()
    fun2()
main()

#WIHTOUT USING MAIN DEF FUNC
def fun1():
    print("Hello")
def fun2():
    print("Welcome")
fun1()
fun2()


