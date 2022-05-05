import sys
n=int(sys.stdin.readline())

nums=[int(x) for x in sys.stdin.readline().split()]
dp=[-100000000 for _ in range(n)]

dp[0]=nums[0]
for i in range(1,n):
    dp[i]=max(dp[i-1]+nums[i],nums[i])
print(max(dp))