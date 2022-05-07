import sys
n,h=map(int,sys.stdin.readline().split(" "))
m=[list(map(int,input())) for _ in range(h)]

visit=[[n*h for _ in range(n)] for _ in range(h)]
visit[0][0]=0
q=[]
q.append([0,0])

while(len(q)!=0):
    now=q[0]
    q.pop(0)

    if(now[0]<h-1):
        if(m[now[0]+1][now[1]]==0 and visit[now[0]+1][now[1]]>visit[now[0]][now[1]]):
            visit[now[0]+1][now[1]]=visit[now[0]][now[1]]
            q.append([now[0]+1,now[1]])
        if(m[now[0]+1][now[1]]==1 and visit[now[0]+1][now[1]]>visit[now[0]][now[1]]+1):
            visit[now[0]+1][now[1]]=visit[now[0]][now[1]]+1
            q.append([now[0]+1,now[1]])
    if(now[1]<n-1):
        if(m[now[0]][now[1]+1]==0 and visit[now[0]][now[1]+1]>visit[now[0]][now[1]]):
            visit[now[0]][now[1]+1]=visit[now[0]][now[1]] 
            q.append([now[0],now[1]+1]) 
        if(m[now[0]][now[1]+1]==1 and visit[now[0]][now[1]+1]>visit[now[0]][now[1]]+1):
            visit[now[0]][now[1]+1]=visit[now[0]][now[1]]+1 
            q.append([now[0],now[1]+1])
    if(now[0]>0):
        if(m[now[0]-1][now[1]]==0 and visit[now[0]-1][now[1]]>visit[now[0]][now[1]]):
            visit[now[0]-1][now[1]]=visit[now[0]][now[1]]
            q.append([now[0]-1,now[1]])
        if(m[now[0]-1][now[1]]==1 and visit[now[0]-1][now[1]]>visit[now[0]][now[1]]+1):
            visit[now[0]-1][now[1]]=visit[now[0]][now[1]]+1
            q.append([now[0]-1,now[1]])
    if(now[1]>0):
        if(m[now[0]][now[1]-1]==0 and visit[now[0]][now[1]-1]>visit[now[0]][now[1]]):
            visit[now[0]][now[1]-1]=visit[now[0]][now[1]] 
            q.append([now[0],now[1]-1]) 
        if(m[now[0]][now[1]-1]==1 and visit[now[0]][now[1]-1]>visit[now[0]][now[1]]+1):
            visit[now[0]][now[1]-1]=visit[now[0]][now[1]]+1 
            q.append([now[0],now[1]-1])
print(visit[h-1][n-1])