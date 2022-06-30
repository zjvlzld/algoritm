Y,X=map(int,input().split(' '))

pan=[] #지도를 저장할 변수
for _ in range(Y):
    pan.append(input())
ans=0#최대 길이
def dfs(y,x,before):#죄표와 이전에 방문했던 문자열을 변수로 준다
    global ans
    dx=[0,0,1,-1]
    dy=[-1,1,0,0]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if(0<=ny<Y and 0<=nx<X and pan[ny][nx] not in before):#다음 방문할 곳의 문자열이 이전 문자열에 없으면
            dfs(ny,nx,before+pan[ny][nx])#방문한다
    if(len(before)>ans):#현재 값이 이전 최대 값보다 길면 정답을 현재의 길이로 치환
        ans=len(before)

dfs(0,0,pan[0][0])#0,0부터 방문

print(ans)