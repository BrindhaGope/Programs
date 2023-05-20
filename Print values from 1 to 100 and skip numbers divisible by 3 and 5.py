i=1
for i in range(100):
    if (i%3!=0) and (i%5!=0):
        print(i)
        i=i+1


i=1
while i<=100:
    if i%3==0 or i%5==0:
        pass
    else:
        print(i)
    i=i+1
