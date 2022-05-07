import sys
n=int(sys.stdin.readline())

visit=[1001 for _ in range(1001)]

visit[1]=0


q=[1]

while(len(q)!=0):
    now=q[0]
    q.pop(0)
    if(now>0 and visit[now-1]>visit[now]+1):
        q.append(now-1)
        visit[now-1]=visit[now]+1
    for i in range(1,1001):
        if(now*(i+1)>1000):
            break
        if(visit[now*(i+1)]>visit[now]+1+i):
            q.append(now*(i+1))
            visit[now*(i+1)]=visit[now]+1+i
print(visit[n])