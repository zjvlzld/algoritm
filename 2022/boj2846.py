n=int(input())
nums=[int(x) for x in input().split(' ')]

ans=0
t=0
for i in range(1,n):
    if nums[i]>nums[i-1]:
        ans=max(ans,nums[i]-nums[t])
    else:
        t=i
print(ans)