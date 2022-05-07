import sys

n,d=map(int, sys.stdin.readline().split(" "))
visit=[-1 for _ in range(100001)]
q=[]

visit[n]=n
q.append(n)
while len(q)!=0:
    now=q[0]
    if(now==d):
        ans=str(now)
        ans0=0
        while now!=n:
            ans=str(visit[now])+" "+ans
            now=visit[now]
            ans0+=1
        print(ans0)
        print(ans)
        exit()
    if(now<100000 and visit[now+1]==-1):
        visit[now+1]=now
        q.append(now+1)
    if(now*2<=100000 and visit[now*2]==-1):
        visit[now*2]=now
        q.append(now*2) 
    if(now>0 and visit[now-1]==-1):
        visit[now-1]=now
        q.append(now-1)
    q.pop(0)