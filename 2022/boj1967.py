n=int(input())
m=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c=map(int, input().split(' '))
    m[a].append([b,c])
    m[b].append([a,c])

visit=[0 for _ in range(n+1)]

far=[1,0]
visit=[0 for _ in range(n+1)]

q=[[1,0]]
visit[1]=1
while len(q)!=0:
    now=q[0]
    q.pop(0)
    if(now[1]>far[1]):
        far=now
    for i in m[now[0]]:
        if visit[i[0]]==0:
            visit[i[0]]=1
            q.append([i[0],now[1]+i[1]])
visit=[0 for _ in range(n+1)]
q=[[far[0],0]]
visit[far[0]]=1

while len(q)!=0:
    now=q[0]
    q.pop(0)
    if(now[1]>far[1]):
        far=now
    for i in m[now[0]]:
        if visit[i[0]]==0:
            visit[i[0]]=1
            q.append([i[0],now[1]+i[1]])
print(far[1])
