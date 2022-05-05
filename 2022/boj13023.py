import sys
a,b=map(int,sys.stdin.readline().split(" "))


m=[[]for _ in range(a)]
visit=[0 for _ in range(a)]

for i in range(b):
    x,y=map(int,sys.stdin.readline().split(" "))
    m[x].append(y)
    m[y].append(x)
def dfs(now,count):
    global visit
    visit[now]=1
    if(count>=5):
        print(1)
        exit()
    for i in m[now]:
        if(visit[i]==0):
            visit[i]=1
            dfs(i,count+1)
            visit[i]=0
    return

for i in range(a):
    dfs(i,1)
    visit[i]=0
print(0)
