import sys
n=int(sys.stdin.readline())

nums=[int(x) for x in sys.stdin.readline().split(" ")]
nums.insert(0,0)
dp=[0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(0,i):
        if(nums[i]>nums[j] and dp[j]+nums[i]>dp[i]):
            dp[i]=dp[j]+nums[i]

print(max(dp))
