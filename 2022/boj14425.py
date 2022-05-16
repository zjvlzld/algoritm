import sys
n,m=map(int,sys.stdin.readline().split(' '))

ns=set()
for i in range(n):
    ns.add(sys.stdin.readline())

ans=0
for _ in range(m):
    get=sys.stdin.readline()
    if(get in ns):
        ans+=1
print(ans)