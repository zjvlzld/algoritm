import sys
n=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]

dp1=[1 for _ in range(n)]
dp2=[1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if(nums[i]>nums[j] and dp1[i]<dp1[j]+1):
            dp1[i]=dp1[j]+1

for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        if(nums[i]>nums[j] and dp2[i]<dp2[j]+1):
            dp2[i]=dp2[j]+1
ans=0
for i in range(n):
    if(ans<dp1[i]+dp2[i]):
        ans=dp1[i]+dp2[i]
print(ans-1)