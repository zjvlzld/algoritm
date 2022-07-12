T=int(input())

for test in range(1,T+1):
    ans=0
    a,b=map(int,input().strip().split(' '))
    m=[]
    for _ in range(a):
        m.append([int(x) for x in input().strip().split(' ')])
    for i in range(a-b+1):
        for j in range(a-b+1):
            t=0
            for k in range(b):
                for l in range(b):
                    t+=m[i+k][j+l]
            ans=max(ans,t)

    print(f"#{test} {ans}")