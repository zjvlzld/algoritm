import sys

a,b=map(int,sys.stdin.readline().split(" "))

m=[[0 for _ in range(a+1)] for _ in range(a+1)]
visit=[0 for _ in range(a+1)]
for _ in range(b):
    x,y=map(int, sys.stdin.readline().split(" "))
    m[x][y]=1
    m[y][x]=1

visit[0]=-1
put=0
count=0
for i in range(1,a+1):
    if(visit[i]==0):
        put+=1
        q=[]
        q.append(i)
        visit[i]=put
        while(len(q)!=0):
            for j in range(a+1):
                if(visit[j]==0 and m[q[0]][j]==1):
                    q.append(j)
                    visit[j]=put
            q.pop(0)
print(put)



