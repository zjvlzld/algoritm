T,goal=[int(x) for x in(input().split(" "))]

nums=[int(x) for x in input().split(" ")]
ans = 0
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if(goal>=nums[i]+nums[j]+nums[k] and ans<nums[i]+nums[j]+nums[k]):
                ans=nums[i]+nums[j]+nums[k]
print(ans)
