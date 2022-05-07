import sys
s,d=map(int,sys.stdin.readline().split(" "))

visit=[100001 for _ in range(100001)]

visit[s]=0

q=[s]


while(len(q)!=0):
    now=q[0]
    q.pop(0)

    if(now>0 and visit[now-1]>visit[now]+1):
        visit[now-1]=visit[now]+1
        q.append(now-1)
    if(now+1<100001 and visit[now+1]>visit[now]+1):
        visit[now+1]=visit[now]+1
        q.append(now+1)
    if(now*2<100001 and visit[now*2]>visit[now]):
        visit[now*2]=visit[now]
        q.append(now*2)
print(visit[d])