from collections import deque
for test in range(1,11):
    ans=0
    m=[[]for _ in range(101)]
    l,s=map(int,input().split())
    get=list(map(int,input().split()))
    for i in range(l//2):
        if(get[i*2+1] not in m[get[i*2]]):
            m[get[i*2]].append(get[i*2+1])
    q=deque()
    visit=[0 for _ in range(101)]
    ans=[s,0]
    visit[s]=1
    q.append([s,0])
    while(len(q)!=0):
        now=q.popleft()
        for i in m[now[0]]:
            if(visit[i]==0):
                visit[i]=1
                q.append([i,now[1]+1])
                if(ans[1]<now[1]+1):
                    ans=[i,now[1]+1]
                elif(ans[1]==now[1]+1):
                    if(ans[0]<i):
                        ans=[i,now[1]+1]
    print(f"#{test} {ans[0]}")