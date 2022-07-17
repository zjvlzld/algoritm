from collections import deque
T=int(input())

for test in range(1,T+1):
    ans=0
    a,b,c,d=map(int, input().rstrip().split(' '))
    m1=[[]for _ in range(a+1)]
    m2=[[]for _ in range(a+1)]
    get=list(int(x) for x in input().rstrip().split(' '))
    for i in range(len(get)//2):
        m1[get[i*2]].append(get[i*2+1])
        m2[get[i*2+1]].append(get[i*2])
    visit=[0 for _ in range(a+1)]
    visit[c]=1
    q=deque()
    q.append(c)
    while(len(q)!=0):
        now=q.popleft()
        for i in m2[now]:
            if(visit[i]==0):
                q.append(i)
                visit[i]=1
    q.append(d)
    visit[d]=1
    common=-1
    while(len(q)!=0):
        now=q.popleft()
        check=False
        for i in m2[now]:
            if(visit[i]==0):
                q.append(i)
                visit[i]=1
            else:
                common=i
                check=True
        if(check):
            break
    visit=[0 for _ in range(a+1)]
    q.clear()
    q.append(common)
    visit[common]=1
    ans+=1
    while(len(q)!=0):
        now=q.popleft()
        for i in m1[now]:
            if(visit[i]==0):
                q.append(i)
                visit[i]=1
                ans+=1
    print(f"#{test} {common} {ans}")