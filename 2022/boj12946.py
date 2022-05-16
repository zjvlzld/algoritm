import sys
sys.setrecursionlimit(1000000)
n=int(sys.stdin.readline())

m = [input() for _ in range(n)]

visit=[[-1]*n for _ in range(n)]
dy=[-1,-1,0,0,1,1]
dx=[0,1,-1,1,-1,0]
ans=0

def dfs(y,x,c):
    global ans
    visit[y][x]=c
    ans=max(ans,1)
    for i in range(6):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=nx<n and 0<=ny<n):
            if(m[ny][nx]=='X'):
                if(visit[ny][nx]==-1):
                    dfs(ny,nx,1-c)
                ans=max(ans,2)
                if(visit[ny][nx]==c):
                    ans=max(ans,3)

for i in range(n):
    for j in range(n):
        if(m[i][j]=="X" and visit[i][j]==-1):
            dfs(i,j,0)

print(ans)
