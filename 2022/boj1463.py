n=int(input())


dp=[1000000 for _ in range(1000001)]
dp[1]=0
dp[2]=1
dp[3]=1
for i in range(4,n+1):
    dp[i]=min(dp[i-1],dp[i])
    if i%2==0:
        dp[i]=min(dp[i//2],dp[i-1])
    if(i%3==0):
        dp[i]=min(dp[i],dp[i//3])
    dp[i]+=1
print(dp[n])
