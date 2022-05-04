import sys

n=int(sys.stdin.readline())
dp=[[0 for _ in range(n)] for _ in range(n) ]

get=[int(x) for x in sys.stdin.readline().split(" ")]
dp[0][0]=get[0]

for i in range(1,n):
    get=[int(x) for x in sys.stdin.readline().split(" ")]
    dp[i][0]=dp[i-1][0]+get[0]
    for j in range(1,i):
        dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+get[j]
    dp[i][i]=dp[i-1][i-1]+get[i]

print(max(dp[n-1]))