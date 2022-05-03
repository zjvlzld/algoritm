t=int(input())

nums=[int(x) for x in input().split(" ")]

for i in range(t-1,0,-1):
    if(nums[i]<nums[i-1]):
        after=nums[i:]
        c=nums[i]
        for j in after:
            if(nums[i-1]>j and c<j):
                c=j
        after.remove(c)
        after.append(nums[i-1])
        after.sort(reverse=True)
        
        for p in range(0,i-1):
            print(nums[p], end=" ")
        print(c,end=" ")
        for t in after:
            print(t,end=" ")
        exit()
print(-1)