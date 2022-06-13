
n=int(input())
m=[[]for _ in range(n+1)]

for _ in range(n):
    get=list(map(int,input().split(' ')))
    for i in range(1,len(get)-1,2):
        m[get[0]].append( [get[i],get[i+1]] )
far=[0,0]
visit=[0 for _ in range(n+1)]
def dfs(now,add):
    global far
    if(add>far[1]):
        far=[now,add]
    for i in m[now]:
        if visit[i[0]]==0:
            visit[i[0]]=1
            dfs(i[0],add+i[1])
visit[1]=1
dfs(1,0)

visit=[0 for _ in range(n+1)]
visit[far[0]]=1
dfs(far[0],0)
print(far[1])
