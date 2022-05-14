import sys

n=int(sys.stdin.readline())

ans=[-1 for _ in range(n+1)]
route=[[] for _ in range(n+1)]

for _ in range(n):
    a,b=map(int, sys.stdin.readline().split(" "))
    route[a].append(b)
    route[b].append(a)
def cicle(now,stack):
    t=stack[:]
    t.append(now)
    for i in route[now]:
        if i in t and i !=t[-2]:
            for j in range(len(t)-1,-1,-1):
                if(j==i):
                    ans[i]=0
                    return
                ans[t[j]]=0
        if not (i in t):
            cicle(i,t)
    return


def dfs(now,stack):
    t=stack[:]
    if(ans[now]!=-1):
        for i in range(1,len(t)):
            ans[stack[i]]=len(stack)-i+ans[now]
       # print(ans,stack)

        return
    t.append(now)
    for i in route[now]:
        if(i !=stack[-1]):
            dfs(i,t)
    
cicle(1,[-1])
for i in range(1,n+1):
    if(len(route[i])==1):
        dfs(i,[-1])

for i in range(1,n+1):
    print(ans[i],end=" ")
print()