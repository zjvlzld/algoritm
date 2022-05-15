import sys

n= int(sys.stdin.readline())

visit=[[0 for _ in range(n)]for _ in range(n)]

sx,sy,ex,ey=map(int,sys.stdin.readline().split(" "))
q=[]

q.append([sx,sy,0])
visit[sx][sy]=1
dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]
while(len(q)!=0):
    now=q[0]
    q.pop(0)
    if(now[0]==ex and now[1]==ey):
        print(now[2])
        exit()
    for i in range(6):
        nextX=now[0]+dx[i]
        nextY=now[1]+dy[i]
        if(0<=nextX<n and 0<=nextY<n and visit[nextX][nextY]==0):
            visit[nextX][nextY]=1
            q.append([nextX,nextY,now[2]+1])

print(-1)