

import copy
n=int(input())
p=[]
for _ in range(n):
    p.append([int(x) for x in input().split(' ')])
ans=0
def solution(d,np):
    global ans
    if(d==5):
        for i in np:
            for j in i:
                ans=max(ans,j)
        return
    #왼쪽으로
    now=copy.deepcopy(np)
    for i in range(n):
        for j in range(n):
            if(now[i][j]!=0):
                for t in range(j):
                    if(now[i][t]==0):
                        now[i][t]=now[i][j]
                        now[i][j]=0
                        break
    for i in range(n):
        for j in range(n-1):
            if now[i][j]==now[i][j+1]:
                now[i][j]=now[i][j]*2
                now[i][j+1]=0
    for i in range(n):
        for j in range(n):
            if(now[i][j]!=0):
                for t in range(j):
                    if(now[i][t]==0):
                        now[i][t]=now[i][j]
                        now[i][j]=0
                        break
    solution(d+1,now)

    #오른쪽으로
    now=copy.deepcopy(np)
    for i in range(n):
        for j in range(n-1,-1,-1):
            if(now[i][j]!=0):
                for t in range(n-1,j,-1):
                    if(now[i][t]==0):
                        now[i][t]=now[i][j]
                        now[i][j]=0
                        break
    for i in range(n):
        for j in range(n-1,0,-1):
            if now[i][j]==now[i][j-1]:
                now[i][j]=now[i][j]*2
                now[i][j-1]=0
    for i in range(n):
        for j in range(n-1,-1,-1):
            if(now[i][j]!=0):
                for t in range(n-1,j,-1):
                    if(now[i][t]==0):
                        now[i][t]=now[i][j]
                        now[i][j]=0
                        break
    solution(d+1,now)

    #위로
    now=copy.deepcopy(np)
    for j in range(n):
        for i in range(n):
            if(now[i][j]!=0):
                for t in range(i):
                    if(now[t][j]==0):
                        now[t][j]=now[i][j]
                        now[i][j]=0
                        break

    for j in range(n):
        for i in range(n-1):
            if now[i][j]==now[i+1][j]:
                now[i][j]=now[i][j]*2
                now[i+1][j]=0

    for j in range(n):
        for i in range(n):
            if(now[i][j]!=0):
                for t in range(i):
                    if(now[t][j]==0):
                        now[t][j]=now[i][j]
                        now[i][j]=0
                        break
    solution(d+1,now)

    #아래로
    now=copy.deepcopy(np)
    for j in range(n):
        for i in range(n-1,-1,-1):
            if(now[i][j]!=0):
                for t in range(n-1,i,-1):
                    if(now[t][j]==0):
                        now[t][j]=now[i][j]
                        now[i][j]=0
                        break
    for j in range(n):
        for i in range(n-1,0,-1):
            if now[i][j]==now[i-1][j]:
                now[i][j]=now[i][j]*2
                now[i-1][j]=0
    for j in range(n):
        for i in range(n-1,-1,-1):
            if(now[i][j]!=0):
                for t in range(n-1,i,-1):
                    if(now[t][j]==0):
                        now[t][j]=now[i][j]
                        now[i][j]=0
                        break
    solution(d+1,now)
solution(0,p)
print(ans)