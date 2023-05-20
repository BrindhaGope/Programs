names=('Navin','Harsh','Kiran','Navin')
comp=('Dell','Apple','MS','Dell')

a=zip(names,comp)
b=list(zip(names,comp))
c=set(zip(names,comp))
d=dict(zip(names,comp))

for (a,b) in a:
    print(a,b)
print()
print(a,'a')
print(b,'b')
print(c,'c')
print(d,'d')



