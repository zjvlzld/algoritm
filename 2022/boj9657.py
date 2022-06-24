n=int(input())
dp=[-1 for _ in range(n+1)]

dp[1]=0
dp[2]=1
dp[3]=0
dp[4]=0
for i in range(5,n+1):
    if(dp[i-1]==1 and dp[i-3]==1 and dp[i-4]==0):
        dp[i]=0
    else:
        dp[i]=1
if(dp[n]==1):
    print('SK')
else:
    print('CY')