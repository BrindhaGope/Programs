a=int(input("Enter a digit:"))
if a==1:
    print("Not a prime number")
if a>1:
    pass
    for i in range(2,a):
      if a%2==0:
        print("Not a prime number")
        break
    else:
        print("Prime number")



