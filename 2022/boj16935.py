import sys
import copy
x,y,c=map(int,sys.stdin.readline().split(" "))

nums=[]
for _ in range(x):
    nums.append([int(i) for i in sys.stdin.readline().split(" ")])

def sol1():
    global nums
    for i in range(len(nums)//2):
        temp=nums[i].copy()
        nums[i]=nums[len(nums)-1-i]
        nums[len(nums)-1-i]=temp
    return

def sol2():
    for i in range(len(nums)):
        for j in range(len(nums[0])//2):
            t=nums[i][j]
            nums[i][j]=nums[i][len(nums[0])-j-1]
            nums[i][len(nums[0])-j-1]=t
    return
def sol3():
    global nums
    temp=copy.deepcopy(nums)
    nums=[]
    for j in range(len(temp[0])):
        put=[]
        for i in range(len(temp)-1,-1,-1):
            put.append(temp[i][j])
        nums.append(put)
    return
def sol4():
    global nums
    temp=copy.deepcopy(nums)
    nums=[]
    for j in range(len(temp[0])-1,-1,-1):
        put=[]
        for i in range(len(temp)):
            put.append(temp[i][j])
        nums.append(put)
    return
def sol5():
    temp=copy.deepcopy(nums)
    for i in range(len(temp)//2):
        for j in range(len(temp[0])//2):
            nums[i][j]=temp[i+len(temp)//2][j]
            nums[i][j+len(temp[0])//2]=temp[i][j]
            nums[i+len(temp)//2][j+len(temp[0])//2]=temp[i][j+len(temp[0])//2]
            nums[i+len(temp)//2][j]=temp[i+len(temp)//2][j+len(temp[0])//2]
    return
def sol6():
    temp=copy.deepcopy(nums)
    for i in range(len(temp)//2):
        for j in range(len(temp[0])//2):
            nums[i][j]=temp[i][j+len(temp[0])//2]
            nums[i][j+len(temp[0])//2]=temp[i+len(temp)//2][j+len(temp[0])//2]
            nums[i+len(temp)//2][j+len(temp[0])//2]=temp[i+len(temp)//2][j]
            nums[i+len(temp)//2][j]=temp[i][j]
    return

do=[int(x) for x in sys.stdin.readline().split(" ")]

for i in do:
    if(i==1):
        sol1()
    if(i==2):
        sol2()
    if(i==3):
        sol3()
    if(i==4):
        sol4()
    if(i==5):
        sol5()
    if(i==6):
        sol6()

for z in nums:
    for i in z:
        print(i,end=" ")
    print()