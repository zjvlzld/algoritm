import sys
sys.setrecursionlimit(100000000)

m=[]

a,b=map(int,input().split(' '))
m=[[]for _ in range(a+1)]
c=[0 for _ in range(a+1)]
visit=[0 for _ in range(a+1)]
for _ in range(b):
    get1,get2=map(int,input().split(' '))
    m[get2].append(get1)
    c[get1]+=1
def dfs(now):
    visit[now]=1
    for i in m[now]:
        if(visit[i]==0):
            dfs(i)
    print(now,end=" ")

for i in range(1,a+1):
    if(c[i]==0 and visit[i]==0):
        dfs(i)

