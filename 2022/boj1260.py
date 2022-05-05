import sys
n,g,s=map(int,sys.stdin.readline().split(" "))

m=[[0 for _ in range(n+1)]for _ in range(n+1)]

for _ in range(g):
    a,b=map(int,sys.stdin.readline().split(" "))
    m[a][b]=1
    m[b][a]=1

visit=[0 for _ in range(n+1)]
def dfs(s):
    global visit
    print(s, end=" ")
    visit[s]=1
    for i in range(n+1):
        if(m[s][i]==1 and visit[i]==0):
            dfs(i)
    return

def bfs(s):
    visit=[0 for _ in range(n+1)]
    q=[]
    q.append(s)
    visit[q[0]]=1

    while(len(q)!=0):
        print(q[0],end=" ")
        for i in range(n+1):
            if(m[q[0]][i]==1 and visit[i]==0):
                visit[i]=1

                q.append(i)
        q.pop(0)   
    return
dfs(s)
print()
bfs(s)