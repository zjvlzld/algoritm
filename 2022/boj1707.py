import sys
sys.setrecursionlimit(10**6)
T=int(sys.stdin.readline())
visit=[]
a=0
b=0
m=[]
def dfs(now,depth):
    global visit
    global a
    global b
    visit[now]=depth
    ans=True
    for i in m[now]:
        if(visit[i]==0):
            ans=dfs(i,depth+1) and ans

        elif(visit[i]!=0):
            if((depth-visit[i])%2==0):
                return False
    return ans


for _ in range(T):
    a,b=map(int,sys.stdin.readline().split(" "))
    m=[[]for _ in range(a+1)]

    for _ in range(b):
        q,w=map(int, sys.stdin.readline().split(" "))
        m[q].append(w)
        m[w].append(q)
    ans=True
    visit=[0 for _ in range(a+1)]
    for i in range(1,a+1):
        if(visit[i]==0):
            ans=ans and dfs(i,1)
    if(ans):
        print('YES')
    else:
        print('NO')    

