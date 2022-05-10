import sys

dp=[[0 for _ in range(101)]for _ in range(101)]

T=int(sys.stdin.readline())

for _ in range(T):
    points=[]
    x,y,d,c=map(int,sys.stdin.readline().split(" "))
    points.append([x,y])
    if(d==0):
        points.append([x+1,y])
    if(d==1):
        points.append([x,y-1])
    if(d==2):
        points.append([x-1,y])
    if(d==3):
        points.append([x,y+1])
    
    for _ in range(c):
        end=points[-1]
        for i in range(len(points)-2,-1,-1):
            points.append([end[0]+end[1]-points[i][1],end[1]-end[0]+points[i][0]])
    for i in points:
        dp[i[0]][i[1]]=1
ans=0
for i in range(100):
    for j in range(100):
        if(dp[i][j]+dp[i+1][j]+dp[i+1][j+1]+dp[i][j+1]==4):
            ans+=1
print(ans)