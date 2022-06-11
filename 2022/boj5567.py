from ast import BitXor


n=int(input())
l=int(input())
m=[[]for _ in range(n+1)]
for _ in range(l):
    a,b=map(int,input().split(' '))
    m[a].append(b)
    m[b].append(a)

visit=[0 for _ in range(n+1)]
q=[]
q.append([1,0])
visit[1]=1
ans=0
while len(q)!=0 and q[0][1]<3:
    now=q[0]
    q.pop(0)
    ans+=1
    for i in m[now[0]]:
        if visit[i]==0:
            visit[i]=1
            q.append([i,now[1]+1])
print(ans-1)