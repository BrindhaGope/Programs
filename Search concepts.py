# LINEAR SEARCH USING FOR LOOP
pos=0
def search(list,n):
    for i in range (len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    else:
        return False

list=[5,3,7,8,9,2]
n=9
if search (list,n):
    print("Found",pos)
else:
    print("Not Found")


# TO PRINT LINEAR SEARCH USING WHILE LOOP
pos=0
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i+=1
    else:
        return False

list=[5,3,7,8,9,2]
n=9
if search (list,n):
    print("Found",pos)
else:
    print("Not Found")

# BINARY SEARCH
pos=-1
def search (list,n):
    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
                return False


list=[4,7,9,23,67,98]
n=67
if search (list,n):
    print("Found",pos)
else:
    print("Not found")


# BUBBLE SORT
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp


nums=[5,6,8,7,3,2]
sort(nums)
print(nums)


# SELECTION SORT
def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j

        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
        print(nums) # to show each iteration

nums=[5,3,8,6,7,2]
sort(nums)
print(nums)


