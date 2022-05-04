import sys

a,b=map(int, sys.stdin.readline().split(" "))

dp=[[0 for _ in range(a+1)]for _ in range(b)]

dp[0]=[1 for _ in range(a+1)]
for i in range(1,b):
    for j in range(a+1):
        for k in range(a+1):
            if(j-k>=0):
                dp[i][j]+=dp[i-1][k]
print(dp[b-1][a])