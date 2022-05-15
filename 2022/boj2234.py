import sys

n,m=map(int, sys.stdin.readline().rstrip().split(' '))
wall=[]
for _ in range(m):
    wall.append([int(x) for x in sys.stdin.readline().rstrip().split(' ')])

visit=[[0 for _ in range(n)]for _ in range(m)]

p=0
count=0
route=[1,2,4,8]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
def dfs(y,x,check):
    visit[y][x]=check
    for i in range(4):
        nx=x+dx[i]  
        ny=y+dy[i]
        if(wall[y][x]&route[i]==0 and visit[ny][nx]==0):
            dfs(ny,nx,check)


nums=[0 for _ in range(n*m+1)]
for i in range(m):
    for j in range(n):
        if(visit[i][j]==0):
            count+=1
            dfs(i,j,count)
for i in range(m):
    for j in range(n):
        nums[visit[i][j]]+=1
lastAns=0
for i in range(m):
    for j in range(n):
        if(j+1<n):
            if(visit[i][j]!=visit[i][j+1]):
                lastAns=max(lastAns,nums[visit[i][j]]+nums[visit[i][j+1]])
        if(i+1<m):
            if(visit[i][j]!=visit[i+1][j]):
                lastAns=max(lastAns,nums[visit[i][j]]+nums[visit[i+1][j]])
# for i in visit:
#     print(i)
# print()
# print(nums)
print(count)
print(max(nums))
print(lastAns)

