import sys
from collections import deque

n=int(sys.stdin.readline())
m=[[]for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split(" "))
    m[a].append(b)
    m[b].append(a)

visit=[0 for _ in range(n+1)]

st=deque()

nums=[int(x) for x in sys.stdin.readline().split(" ")]
if(nums[0]!=1):
    print(0)
    exit()
st.append(1)
visit[1]=1
for i in range(1,n):
    now=nums[i]
    if visit[now]==1:
        print(0)
        exit()
    if(now not in m[st[-1]]):
        print(0)
        exit()
    else:
        st.append(now)
        visit[now]=1
    while True and len(st)!=0:
        checkNow=st[-1]
        check=False
        for i in m[checkNow]:
            if(visit[i]==0):
                check=True
                break
        if(check):
            break
        st.pop()
print(1)
