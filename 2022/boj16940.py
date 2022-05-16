import sys
from collections import deque
n=int(sys.stdin.readline())
m=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split(' '))
    m[a].append(b)
    m[b].append(a)

visit=[int(x) for x in sys.stdin.readline().split(" ")]

visited=[0 for _ in range(n+1)]
q=deque()
visited[1]=1
for i in m[1]:
    m[i].remove(1)
q.append(m[1])
pointNow=0
while(len(q)!=0):
    now=q.popleft()
    for i in range(len(now)):
        pointNow+=1
        if(pointNow==n):
            exit()
        if(not visit[pointNow] in now):

            print(0)
            exit()
        else:
            if(visited[visit[pointNow]]==1):

                print(0)
                exit()
            else:
                for i in m[visit[pointNow]]:
                    m[i].remove(visit[pointNow])
                q.append(m[visit[pointNow]])
                visited[visit[pointNow]]=1

print(1)