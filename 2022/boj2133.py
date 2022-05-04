import sys
n=int(sys.stdin.readline())

dp=[0 for _ in range(31)]

dp[2]=3
for i in range(3,31):
    for j in range(4,31,2):
        if(i-j==0):
            dp[i]+=2
        else:
            dp[i]+=dp[i-j]*2
    dp[i]+=dp[i-2]*3
print(dp)
print(dp[n])