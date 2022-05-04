import sys
n=int(sys.stdin.readline())
cost=[int(x) for x in sys.stdin.readline().split(" ")]

cost.insert(0,10000000)
dp=[10000000 for _ in range(n+1)]
dp[0]=0
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+cost[j])

print(dp[n])