import sys

dp=[0 for _ in range(5001)]
dp[0]=1
dp[2]=1
for i in range(4,5001,2):
    for j in range(0,i,2):
        dp[i]+=(dp[j]*dp[i-2-j])%1000000007

t= int(sys.stdin.readline())
for _ in range(t):
    get=int(sys.stdin.readline())
    print(dp[get])