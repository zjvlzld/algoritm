import sys
n=int(sys.stdin.readline())
wheel=[]

for _ in range(n):
    wheel.append(list(map(int,input())))

order=int(sys.stdin.readline())

for _ in range(order):
    a,b=map(int,sys.stdin.readline().split(" "))
    do=[0 for _ in range(n)]
    r=0
    do[a-1]=b
    for i in range(a-1,0,-1):
        if(wheel[i][6]==wheel[i-1][2]):
            do[i-1]=0
        else:
            do[i-1]=do[i]*-1
    for i in range(a-1,n-1):
        if(wheel[i][2]==wheel[i+1][6]):
            do[i+1]=0
        else:
            do[i+1]=do[i]*-1
    for i in range(n):
        if(do[i]==0):
            continue
        elif(do[i]==1):
            wheel[i]=wheel[i][-1:]+wheel[i][:-1]
        elif(do[i]==-1):
            wheel[i]=wheel[i][1:]+wheel[i][:1]
ans=0
for i in range(n):
    ans+=wheel[i][0]
print(ans)