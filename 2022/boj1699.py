import sys

n=int(sys.stdin.readline())
dp=[100000 for _ in range(n+1)]
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    for j in range(1,int(i**(1/2)+1)):
        if(dp[i]>dp[i-j**2]+1):
            dp[i]=dp[i-j**2]+1
print(dp[n])
