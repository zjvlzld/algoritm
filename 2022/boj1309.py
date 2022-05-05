import sys

n=int(input())

dp=[1,1,1]

for i in range(1,n):
    before=dp.copy()
    dp[0]=(before[1]+before[2])%9901
    dp[1]=(before[0]+before[2])%9901
    dp[2]=sum(before)%9901
print(sum(dp)%9901)