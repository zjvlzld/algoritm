v,e=map(int,input().split(' '))
s=int(input())
m=[ [] for _ in range(v+1)]
visit=[30000001 for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,input().split(' '))
    m[a].append([b,c])

q=[s]
visit[s]=0
while(len(q)!=0):
    now=q[0]
    q.pop(0)
    for i in m[now]:
        if(visit[now]+i[1]<visit[i[0]]):
            visit[i[0]]=visit[now]+i[1]
            q.append(i[0])

for i in range(1,v+1):
    if(visit[i]==30000001):
        print('INF')
    else:
        print(visit[i])
