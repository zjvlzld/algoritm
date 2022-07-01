T=int(input())

for _ in range(T):
    n=int(input())
    sc=[]
    for _ in range(n):
        a,b=map(int,input().split(' '))
        sc.append([a,b])
    sc.sort(key=lambda x:x[0])
    ans=1
    t=sc[0][1]
    for i in range(1,n):
        if sc[i][1]<t:
            ans+=1
            t=sc[i][1]
    print(ans)