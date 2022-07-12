T=int(input())

for test in range(1,T+1):
    ans=0
    N,K=map(int,input().split(' '))
    m=[]
    check=[[[0,0]for _ in range(N)]for _ in range(N)]
    for _ in range(N):
        m.append( [ int(x) for x in input().strip().split(' ')] )
    for i in range(N):
        for j in range(N):
            if(m[i][j]==1 and check[i][j][0]==0):
                t=0
                while(i+t<N and m[i+t][j]==1 and check[i+t][j][0]==0):
                    check[i+t][j][0]=1
                    t+=1
                if(t==K):
                    ans+=1
            if(m[i][j]==1 and check[i][j][1]==0):
                t=0
                while(j+t<N and m[i][j+t]==1 and check[i][j+t][1]==0):
                    check[i][j+t][1]=1
                    t+=1
                if(t==K):
                    ans+=1
    print(f"#{test} {ans}")