# TO PRINT SQUARE USING FUNC
def square(a):
    return a*a
result=square(5)
print(result)

# TO PRINT SQUARE USING LAMBDA FUNC
f=lambda a:a*a
result=f(6)
print(result)

# TO PRINT ADDITION OF 2 NUMS USING LAMBDA
f=lambda a,b:a+b
result=f(5,6)
print (result)

# PRINT EVEN NUMS USING FILTER
def evens(n):
    return n%2==0
nums=[3,2,5,7,8,6,4]
evens=list(filter(evens,nums))
print(evens)

# PRINT DOUBLE OF A NUM USING MAP
def update(n):
    return n*2
nums=[3,2,5,7,8,6,4]
double=list(map(update,nums))
print (double)

# PRINT SUM OF NUMBERS USING REDUCE
from functools import *
def add(a,b):
    return a+b
nums=[3,2,5,7,8,6,4]
sum =(reduce(add,nums))
print(sum)


# USING FILTER, MAP, REDUCE FUNC IN SINGLE LAMBDA FUNCTION
from functools import*
nums=[3,2,5,7,8,6,4]
even=list(filter(lambda a:a%2==0, nums))
double=list(map(lambda a:a*2, nums))
sum=(reduce(lambda a,b:a+b,nums))
print(even)
print(double)
print(sum)