import queue
import sys
from collections import deque
T=int(sys.stdin.readline())
c=[0 for _ in range(10000)]
sosu=[]
for i in range(2,10000):
    if(c[i]==0):
        if(i>1000):
            sosu.append(i)
        for j in range(i,10000,i):
            c[j]=1


for _ in range(T):
    a,b=map(int,sys.stdin.readline().split(' '))
    visit=[0 for _ in range(10000)]

    visit[a]=1
    q=deque()
    q.append([a,0])
    check=True
    while len(q)!=0 :
        now,count=q.popleft()
        if(now==b):
            print(count)
            check=False
            break
        for i in range(10):
            next1=now%1000+i*10**3
            next2=(now//1000)*1000+i*10**2+now%100
            next3=(now//100)*100+i*10+now%10
            next4=(now//10)*10+i
            if(next1 in sosu and visit[next1]==0):
                q.append([next1,count+1])
                visit[next1]=1
            if(next2 in sosu and visit[next2]==0):
                q.append([next2,count+1])
                visit[next2]=1
            if(next3 in sosu and visit[next3]==0):
                q.append([next3,count+1])
                visit[next3]=1
            if(next4 in sosu and visit[next4]==0):
                q.append([next4,count+1])
                visit[next4]=1
    if(check):
        print(-1)