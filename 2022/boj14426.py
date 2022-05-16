import sys

n,m=map(int,sys.stdin.readline().split(" "))

ns=[]
for _ in range(n):
    ns.append(sys.stdin.readline().rstrip())

ans=0
for _ in range(m):
    get=sys.stdin.readline().rstrip()
    c=len(get)
    for i in range(n):
        if(get==ns[i][:c]):
            ans+=1
            break
print(ans)