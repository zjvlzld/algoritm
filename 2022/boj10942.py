import sys
n=int(sys.stdin.readline())
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
nums=[int(x) for x in sys.stdin.readline().split(' ')]
nums=[1]+nums
for i in range(1,n+1):
    dp[i][i]=1
order=int(sys.stdin.readline())

def solution(s,e):
    if(dp[s][e]!=0):
        return dp[s][e]
    if(s==e):
        return 1
    if(nums[s]==nums[e]):
        if(e-s==1):
            dp[s][e]=1
        else:    
            dp[s][e]=solution(s+1,e-1)
    else:
        dp[s][e]=-1
    return dp[s][e]

for _ in range(order):
    a,b=map(int,sys.stdin.readline().split(" "))
    ans=solution(a,b)
    if(ans==1):
        print(ans)
    else:
        print(0)
