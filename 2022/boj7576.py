import sys
from collections import deque


x,y=map(int, sys.stdin.readline().split())
tomato=[[0 for i in range (x)]for j in range(y)]
for i in range(y):
    tomato[i]=list(map(int,sys.stdin.readline().split()))

que=deque()
for i in range(y):
    for j in range(x):
        if(tomato[i][j]==1):
            que.append([j,i])
dx=[0,0,-1,1]
dy=[1,-1,0,0]
while (len(que)!=0):
    now=que.popleft()
    for i in range(4):
        nx=now[0]+dx[i]
        ny=now[1]+dy[i]
        if(0<=nx<x and 0<=ny<y):
            if(tomato[ny][nx]==0):
                tomato[ny][nx]=tomato[now[1]][now[0]]+1
                que.append([nx,ny])

max=0
check=0
for i in range(y):
    for j in range(x):
        if(tomato[i][j]==0):
            if(check!=1):
               print(-1)
               check=1
        if(tomato[i][j]>max):
            max=tomato[i][j]
if(check!=1):
    print(max-1)



