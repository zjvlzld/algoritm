y,x=map(int,input().split(' '))
m=[]
visit=[[0 for _ in range(x)]for _ in range(y)]
ans=[[0 for _ in range(x)]for _ in range(y)]
for _ in range(y):
    m.append(list(int(x) for x in input().split(' ')))
dx=[1,-1,0,0]
dy=[0,0,-1,1]
for i in range(y):
   for j in range(x):
       if m[i][j]==2:
            q=[[i,j]]
            visit[i][j]=1
            while(len(q)!=0):
               now=q[0]
               q.pop(0)
               for d in range(4):
                   ny=now[0]+dy[d]
                   nx=now[1]+dx[d]
                   if(0<=nx<x and 0<=ny<y):
                       if(visit[ny][nx]==0 and m[ny][nx]!=0):
                           visit[ny][nx]=1
                           ans[ny][nx]=ans[now[0]][now[1]]+1
                           q.append([ny,nx])
            for j in range(y):
                for k in range(x):
                    if(ans[j][k]==0 and m[j][k]==1):
                        print(-1,end=" ")
                    else:
                        print(ans[j][k],end=" ")
                    
                print()
            exit()
