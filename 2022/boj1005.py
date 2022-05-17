import sys
from collections import deque

T= int(sys.stdin.readline())

for _ in range(T):
    a,b=map(int,sys.stdin.readline().split((" ")))
    cost=[int(x) for x in sys.stdin.readline().rstrip().split((" "))]
    cost=[0]+cost
    m=[[]for _ in range(a+1)]
    st=[0 for _ in range(a+1)]
    dp=[-1 for _ in range(a+1)]
    for _ in range(b):
        g1,g2=map(int, sys.stdin.readline().split((" ")))
        m[g2].append(g1)
    # print(m)
    # print(cost)
    end=int(sys.stdin.readline())
    def solution(now):
        if(dp[now]!=-1):
            return dp[now]
        if(len(m[now])==0):
            dp[now]=cost[now]
            return dp[now]
        r=-1
        for i in m[now]:
            r=max(r,solution(i))
        dp[now]=r+cost[now]
        return dp[now]
    print(solution(end))

