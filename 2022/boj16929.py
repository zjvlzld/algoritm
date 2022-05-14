import sys

a,b=map(int,sys.stdin.readline().split(" "))
visit=[[0 for _ in range(b)]for _ in range(a)]
m=[]
for _ in range(a):
    m.append(sys.stdin.readline().rstrip())
def dfs(x,y,beforX,beforY):
    visit[y][x]=1
    if(y+1<a and m[y][x]==m[y+1][x]):
        if(visit[y+1][x]==0):
            dfs(x,y+1,x,y)
        else:
            if(y+1!=beforY):
                print('Yes')
                exit()
    if(x+1<b and m[y][x]==m[y][x+1]):
        if(visit[y][x+1]==0):
            dfs(x+1,y,x,y)
        else:
            if(x+1!=beforX):
                print('Yes')
                exit()
    
    if(y-1>=0 and m[y][x]==m[y-1][x]):
        if(visit[y-1][x]==0):
            dfs(x,y-1,x,y)
        else:
            if(y-1!=beforY):
                print('Yes')
                exit()
    if(x-1>=0 and m[y][x]==m[y][x-1]):
        if(visit[y][x-1]==0):
            dfs(x-1,y,x,y)
        else:
            if(x-1!=beforX):
                print('Yes')
                exit()

for i in range(a):
    for j in range(b):
        if(visit[i][j]==0):
            dfs(j,i,-2,-2)
print('No')