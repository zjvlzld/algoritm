from collections import deque
for test in range(1,11):
    
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    tc=int(input())
    m=[]
    goalX=0
    goalY=0
    for _ in range(16):
        m.append(input())
    visit=[[0 for _ in range(16)]for _ in range(16)]
    q=deque()
    for i in range(16):
        for j in range(16):
            if(m[i][j]=='2'):
                q.append([i,j])
                visit[i][j]=1
            if(m[i][j]=='3'):
                goalY=i
                goalX=j
    while(len(q)!=0):
        now=q.popleft()
        for d in range(4):
            nx=now[1]+dx[d]
            ny=now[0]+dy[d]
            if(0<=nx<16 and 0<=ny<16 and visit[ny][nx]==0 and (m[ny][nx]=='0' or m[ny][nx]=='3')):
                q.append([ny,nx])
                visit[ny][nx]=1
    

#    for i in visit:
#        print(i)
#    print(goalY,goalX)
    if(visit[goalY][goalX]==1):
        print(f"#{test} 1")
    else:
        print(f"#{test} 0")