import sys

dp=[0]*1000001
ans=[0]*1000001
for i in range(1,1000001):
    for j in range(1,1000001):
        if(i*j>1000000):
            break
        dp[i*j]+=i
for i in range(1,1000001):
    ans[i]=ans[i-1]+dp[i]
T=int(sys.stdin.readline().rstrip())
for _ in range(T):
    get=int(sys.stdin.readline().rstrip())
    print(ans[get])
