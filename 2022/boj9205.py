from collections import deque
T=int(input())

for _ in range(T):
    n=int(input())
    q=deque()
    check=True
    a,b=map(int,input().split(' '))
    q.append([a,b])
    con=[]
    visited=[]
    for _ in range(n+1):
        a,b=map(int,input().split(' '))
        con.append([a,b])
        visited.append(0)
    while(len(q)!=0):
        now=q[0]
        q.popleft()
        if(con[-1][0]==now[0] and con[-1][1]==now[1]):
            print('happy')
            check=False
            break
        for i in range(n+1):
            if(visited[i]==0 and (abs(now[0]-con[i][0])+abs(now[1]-con[i][1]))<=1000):
                visited[i]=1
                q.append([con[i][0],con[i][1]])
    if(check):
        print('sad')
