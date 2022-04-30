from cmath import sqrt


while True:
    get=int(input())
    if(get==-1):
        break
    nums=[]
    add=0
    for i in range(1,int((get**(1/2))//1)+1):
        if(get%i==0):
            nums.append(i)
            nums.append(get//i)
            add=add+i+get//i
    nums.sort()
    if(sum(nums)-nums[len(nums)-1]==get):
        nums.sort()
        print(get,'= 1',end="")
        for i in range(1,len(nums)-1):
            print(' +',nums[i],end="")
        print()
    else:
        print(get,'is NOT perfect')
        