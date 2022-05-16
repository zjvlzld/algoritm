import sys

n,k=map(int,sys.stdin.readline().split(" "))

dp=[[1 for _ in range(n+1)]for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][i]=1
    dp[1][i]=i


for i in range(2,k+1):
    for j in range(i+1,n+1):
        dp[i][j]=(dp[i-1][j-1]+dp[i][j-1])%10007
print(dp[k][n]%10007)
