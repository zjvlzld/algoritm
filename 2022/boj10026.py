import sys
from collections import deque

n=int(sys.stdin.readline())
m=[]
for _ in range(n):
    m.append(sys.stdin.readline().rstrip())
visit=[[0 for _ in range(n)]for _ in range(n)]
visit2=[[0 for _ in range(n)]for _ in range(n)]
dx=[0,0,-1,1]
dy=[1,-1,0,0]
ans1=0
ans2=0
for i in range(n):
    for j in range(n):
        if visit[i][j]==0:
            ans1+=1
            q=deque()
            q.append([i,j,ans1])
            visit[i][j]=ans1
            while(len(q)!=0):
                x,y,count=q.popleft()
                now=m[x][y]
                for next in range(4):
                    nextX=x+dx[next]
                    nextY=y+dy[next]
                    if(0<=nextX<n and 0<=nextY<n and now==m[nextX][nextY] and visit[nextX][nextY]==0):
                        q.append([nextX,nextY,count])
                        visit[nextX][nextY]=count
        if visit2[i][j]==0:
            ans2+=1
            q=deque()
            q.append([i,j,ans2])
            visit2[i][j]=ans2
            while(len(q)!=0):
                x,y,count=q.popleft()
                now=m[x][y]
                for next in range(4):
                    nextX=x+dx[next]
                    nextY=y+dy[next]
                    if(0<=nextX<n and 0<=nextY<n and (now!='B')==(m[nextX][nextY]!='B') and visit2[nextX][nextY]==0):
                        q.append([nextX,nextY,count])
                        visit2[nextX][nextY]=count
print(ans1,ans2)
