n=int(input())
t=int(input())
m=[[]for _ in range(n+1)]
visit=[0 for _ in range(n+1)]

for _ in range(t):
    a,b=map(int,input().split(' '))
    m[a].append(b)
    m[b].append(a)

def dfs(now):
    for i in m[now]:
        if visit[i]==0:
            visit[i]=1
            dfs(i)

visit[1]=1
dfs(1)

print(sum(visit)-1)
