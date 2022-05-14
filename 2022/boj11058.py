import sys


n=int(sys.stdin.readline())

dp=[0 for _ in range(n+4)]
for i in range(1,7):
    dp[i]=i

for i in range(7,n+1):
    for j in range(2,5):
        dp[i]=max(dp[i],dp[i-(j+1)]*j)

print(dp[n])