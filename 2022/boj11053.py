import sys
t= int(sys.stdin.readline())

nums=[int(x) for x in sys.stdin.readline().split(" ")]

dp=[1 for _ in range(t)]

for i in range(t):
    for j in range(i+1,t):
        if(nums[i]<nums[j] and dp[j]<dp[i]+1):
            dp[j]=dp[i]+1
print(max(dp))