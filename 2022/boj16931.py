import sys
n,m=map(int,sys.stdin.readline().split(" "))

pan=[]
for _ in range(n):
    pan.append([int(x) for x in sys.stdin.readline().split(" ")])

ans=n*m
#left
for i in range(n):
    ans+=pan[i][0]
    for j in range(1,m):
        if(pan[i][j-1]<pan[i][j]):
            ans+=pan[i][j]-pan[i][j-1]
for j in range(m):
    ans+=pan[0][j]
    for i in range(1,n):
        if(pan[i-1][j]<pan[i][j]):
            ans+=pan[i][j]-pan[i-1][j]
print(ans*2)
