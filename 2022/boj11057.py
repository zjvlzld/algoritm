import sys

n=int(input())

dp=[1,1,1,1,1,1,1,1,1,1]

for i in range(1,n):
    before=dp.copy()
    for i in range(10):
        dp[i]=sum(before[:i+1])%10007
print(sum(dp)%10007)