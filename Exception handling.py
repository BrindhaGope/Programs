# EXCEPTION HANDLING
a=5
b=0

try:
    print("Resource open")
    print(a/b)

    n= int(input("Enter the number:"))
    print(n)
except ZeroDivisionError as e:
    print("Hey, you can't divide a num by zero,e")

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong")

finally:
    print("Resource closed")

# MULTITHREADING
from threading import *
from time import *
class Hello(Thread):
    def run(self): # only use run method name to work
        for i in range(5):
            print("Hello")
            sleep(1) # to print one by one

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1) # to print one by one

o1=Hello()
o2=Hi()

o1.start() # to execute 2 diff methods start used instead run
sleep(0.2)
o2.start()

o1.join() # to avoid collision between both
o2.join()
print("Bye")

# TO WRITE IN OTHER FILE FROM THIS EXISITNG FILE
f = open("DEMO.py", 'r')
f1 = open("ABC.py", 'w')

f1.write("Something")
f1.write("\nPeople")
f1.write("\nLaptop")

# TO COPY FROM 1 FILE TO OTHER
f = open("DEMO.py", 'r')
f1 = open("ABC.py", 'w')

for data in f:
    print(data, end=" ")  # prints everything that is avail in demo file(other file)

# TO PRINT EVERYTHING FROM 1 FILE TO THE OTHER
f = open("DEMO.py", 'r')
f1 = open("ABC.py", 'w')

for data in f:
    f1.write(data)  # to copy and paste data from 1 file to another

# TO COPY IMAGE FROM A FILE TO OTHER
f = open("DEMO.py", 'rb')
f1 = open("ABC.py", 'wb')

for img in f:
    print(img)


