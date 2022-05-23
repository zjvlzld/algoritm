T = int(input())
ans=""
for case in range(1,T+1):
    n=int(input())
    nums=[int(x) for x in input().split()]
    t=0
    for i in range(1,n-1):
        if min(nums[i-1],nums[i+1])<nums[i]<max(nums[i-1],nums[i+1]):
            t+=1
    ans+="#"+str(case)+" "+str(t)+"\n"

print(ans)