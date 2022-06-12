from pickle import TRUE
from tabnanny import check


n=int(input())

pan=[]
for _ in range(n):
    pan.append([int(x) for x in input().split(' ')])

ans=[0,0]
def solution(n,sx,sy):
    if(n==1):
        ans[pan[sx][sy]]+=1
        return
    check=True
    now=pan[sx][sy]
    for i in range(sx,sx+n):
        for j in range(sy,sy+n):
            if pan[i][j]!=now:
                check=False
                break
        if( not check):
            break

    if(check):
        ans[now]+=1
        return
    else:
        solution(n//2,sx,sy)
        solution(n//2,sx+n//2,sy)
        solution(n//2,sx+n//2,sy+n//2)
        solution(n//2,sx,sy+n//2)
solution(n,0,0)
for i in ans:
    print(i)