n=int(input())
cost=[int(x) for x in input().split(" ")]
cost.insert(0,0)
dp=[0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(i+1):
        dp[i]=max(dp[i-j]+cost[j],dp[i])
print(dp[n])    