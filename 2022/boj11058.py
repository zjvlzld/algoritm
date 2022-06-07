import sys

n=int(sys.stdin.readline())

dp=[0 for _ in range(1001)]

dp[1]=1
dp[2]=2
dp[3]=3

for i in range(4,n+1):
    if(dp[i]<dp[i-1]+1):
        dp[i]=dp[i-1]+1
    for j in range(1,i-2):
        dp[i]=max(dp[i],dp[i-2-j]*(j+1))
print(dp[n])