import sys

a,b,d,n=map(int,sys.stdin.readline().split(" "))
dp=[0 for _ in range(n+1)]
dp[0]=1
ans=1
sum=2
for i in range(1,n+1):
    if(i>=b):
        sum-=(dp[i-b]-1000)
        sum%=1000
    if(i>=a):
        sum+=dp[i-a]
        sum%=1000
    dp[i]=sum
    ans+=dp[i]
    if(i>=d):
        ans-=dp[i-d]-1000
        sum%=1000
print(ans%1000)