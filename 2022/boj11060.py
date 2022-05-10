import sys

n=int(sys.stdin.readline())

nums=[int(x) for x in sys.stdin.readline().split(" ")]

dp=[1010 for _ in range(n)]
dp[0]=0
for i in range(n):
    now=nums[i]
    for j in range(now+1):
        if(i+j<n):
            if(dp[i]+1<dp[i+j]):
                dp[i+j]=dp[i]+1

if(dp[n-1]>1009):
    print(-1)
else:   
    print(dp[n-1])