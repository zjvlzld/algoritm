import sys
import copy

N,M,T=map(int,sys.stdin.readline().rstrip().split(" "))

pan=[]

for _ in range(N):
    pan.append([int(x) for x in sys.stdin.readline().split(" ")])

for _ in range(T):
    x,d,k=map(int,sys.stdin.readline().split())
    for i in range(x,N+1,x):
        if(d==0):
            pan[i-1]=pan[i-1][-k:]+pan[i-1][:-k]
        else:
            pan[i-1]=pan[i-1][k:]+pan[i-1][:k]

    # print('돌리고')    
    # for i in pan:
    #     print(i)
    check=True
    t=copy.deepcopy(pan)
    for i in range(N):
        for j in range(M):
            if(i+1<N):
                if(pan[i][j]==pan[(i+1)][j]):
                    if(pan[i][j]!=0):
                        check=False
                    t[i][j]=0
                    t[(i+1)%N][j]=0
            if(i-1>=0):
                if(pan[i][j]==pan[i-1][j]):
                    if(pan[i][j]!=0):
                        check=False
                    t[i][j]=0
                    t[i-1][j]=0

            if(pan[i][j]==pan[i][(j+1)%M]):
                if(pan[i][j]!=0):
                        check=False
                t[i][j]=0
                t[i][(j+1)%M]=0
            if(pan[i][j]==pan[i][j-1]):
                if(pan[i][j]!=0):
                        check=False
                t[i][j]=0
                t[i][j-1]=0
    # print('제거하고')
    # for i in t:
    #     print(i)
    pan=copy.deepcopy(t)
    if(check):
        count=0
        sumNow=0
        for i in range(N):
            for j in range(M):
                if t[i][j]!=0:
                    count+=1
                    sumNow+=t[i][j]
        if(count!=0):
            avgNow=sumNow/count
        #print(avgNow,sumNow,count)
        for i in range(N):
            for j in range(M):
                if(t[i][j]!=0):
                    if((t[i][j])>avgNow):
                        t[i][j]=t[i][j]-1

                    elif(t[i][j]<avgNow):
                        t[i][j]+=1
        #print('평균하고')
        pan=copy.deepcopy(t)
        # for i in pan:
        #     print(pan)

ans=0
for i in pan:
    ans+=sum(i)
print(ans)