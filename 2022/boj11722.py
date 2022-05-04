import sys
n=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]
nums.insert(0,1001)
dp=[0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i):
        if(nums[i]<nums[j] and dp[i]<dp[j]+1):
            dp[i]=dp[j]+1

print(dp)
print(max(dp))
