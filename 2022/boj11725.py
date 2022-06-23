import sys
sys.setrecursionlimit(1000000000)
n=int(input())
m=[[]for _ in range(n+1)]

ans=[-1 for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split(' '))
    m[a].append(b)
    m[b].append(a)

def solution(b,now):
    ans[now]=b
    for i in m[now]:
        if(ans[i]==-1):
            solution(now,i)

solution(0,1)
for i in range(2,n+1):
    print(ans[i])