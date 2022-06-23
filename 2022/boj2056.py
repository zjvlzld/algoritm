n=int(input())
m=[[]for _ in range(n+1)]
t=[0 for _ in range(n+1)]
d=[-1 for _ in range(n+1)]
for i in range(1,n+1):
    get=list(int(x) for x in input().split(' '))
    t[i]=get[0]
    for j in range(2,len(get)):
        m[i].append(get[j])
def solution(now):
    if d[now]!=-1:
        return d[now]
    temp=t[now]
    for i in m[now]:
        temp=max(temp,solution(i)+t[now])
    d[now]=temp
    return d[now]
for i in range(n,0,-1):
    if(d[i]==-1):
        solution(i)
print(max(d))