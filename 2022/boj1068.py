import sys
sys.setrecursionlimit(100000)
n=int(input())
gets=[int(x) for x in input().split(' ')]
m=[[]for _ in range(n)]
for i in range(0,n):
    if(gets[i]!=-1):
        m[gets[i]].append(i)
d=int(input())
ans=0

def soltion(now):
    global ans
    if(len(m[now])==0):
        ans+=1
        return
    if(len(m[now])==1 and m[now][0]==d):
        ans+=1
        return
    for i in m[now]:
        if(i != d):
            soltion(i)

for i in range(n):
    if gets[i]==-1:
        if i!=d:
            soltion(i)
            break
print(ans)