a,b,c=map(int,input().split(" "))
pan=[]
for _ in range(a):
    pan.append([int(x) for x in input().split(" ")])
co=[[0 for _ in range(b)] for _ in range(a)]
ans=-1000000
def solution(check,count,now,x,y):
    global ans
    global a
    global b
    global c
    if count==c:
        if(ans<now):
            ans=now
        return
    if(y==b-1):
        if(x==a-1):
            if(check[x-1][y]==0 and check[x][y-1]==0):
                if count+1==c:
                    now+=pan[x][y]
                    if(ans<now):
                        ans=now
            return
        else:
            solution(check,count,now,x+1,0)
            if(x!=0):
                if(check[x-1][y]==0 and check[x][y-1]==0):
                    check[x][y]=1
                    solution(check,count+1,now+pan[x][y],x+1,0)
                    check[x][y]=0
                return
            else:
                if(check[x][y-1]==0):
                    check[x][y]=1
                    solution(check,count+1,now+pan[x][y],x+1,0)
                    check[x][y]=0
                return
    else:
        solution(check,count,now,x,y+1)
        if(x==0):
            if(y==0):
                check[0][0]=1
                solution(check,count+1,now+pan[x][y],x,y+1)
                check[0][0]=0
                return
            else:
                if(check[x][y-1]==0):
                    check[x][y]=1
                    solution(check,count+1,now+pan[x][y],x,y+1)
                    check[x][y]=0
                return
        else:
            if(y==0):
                if(check[x-1][y]==0):
                    check[x][y]=1
                    solution(check,count+1,now+pan[x][y],x,y+1)
                    check[x][y]=0

                return
            else:
                if(check[x-1][y]==0 and check[x][y-1]==0):
                    check[x][y]=1
                    solution(check,count+1,now+pan[x][y],x,y+1)
                    check[x][y]=0
                return
    return
solution(co,0,0,0,0)
print(ans)