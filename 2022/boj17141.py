import sys
from collections import deque

n,p=map(int,sys.stdin.readline().split())
m=[]
point=[]
ans=2501
check=False
dx=[0,0,1,-1]
dy=[1,-1,0,0]
for _ in range(n):
    m.append([int(x) for x in sys.stdin.readline().rstrip().split(" ")])

for i in range(n):
    for j in range(n):
        if(m[i][j]==2):
            point.append([i,j])
#print(point)
def bfs(points):
    global ans
    visit=[[0 for _ in range(n)] for _ in range(n)]
#    print(points)
    q=deque()
    for i in points:
        q.append([point[i][0],point[i][1],1])
        visit[point[i][0]][point[i][1]]=1
    while len(q)!=0:
        x,y,count=q.popleft()
        for next in range(4):
            nx=x+dx[next]
            ny=y+dy[next]
            if(0<=nx<n and 0<=ny<n and m[nx][ny]!=1 and visit[nx][ny]==0):
                q.append([nx,ny,count+1])
                visit[nx][ny]=count+1
    t=-1
    t1=2501
    for i in range(n):
        for j in range(n):
            if(m[i][j]!=1):
                t=max(t,visit[i][j])
                t1=min(t1,visit[i][j])
    if(t1==0):
        ans=min(2501,ans)
    else:
        ans=min(t,ans)
    return

def dfs(now,count,points):
    if(count==p):
        bfs(points)
        return
    if(now>=len(point)):
        return
    dfs(now+1,count,points)
    t=points[:]+[now]
    dfs(now+1,count+1,t)
    return

dfs(0,0,[])
if(ans==2501):
    print(-1)
else:
    print(ans-1)

