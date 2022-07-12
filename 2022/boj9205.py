from collections import deque
T=int(input())

for _ in range(T):
    n=int(input())
    q=deque()
    check=True ##bfs도중 성공했는지 체크
    a,b=map(int,input().split(' '))
    q.append([a,b])#시작지점을 먼저 큐에 넣는다
    con=[]#편의점의 좌표들 및 페스티벌 좌표
    visited=[]
    for _ in range(n+1):#편의점 좌표와 페스티벌 좌표를 넣는다
        a,b=map(int,input().split(' '))
        con.append([a,b])
        visited.append(0)
    while(len(q)!=0):#bfs
        now=q[0]
        q.popleft()
        if(con[-1][0]==now[0] and con[-1][1]==now[1]):#만약 현재 지점이 페스티벌 장소면
            print('happy')#해피출력
            check=False#출력완료를 체크 한 후
            break#bfs종료
        for i in range(n+1):#아닐경우 노드 전체에서 방문 가능한 노드를 찾는다
            if(visited[i]==0 and (abs(now[0]-con[i][0])+abs(now[1]-con[i][1]))<=1000):
                visited[i]=1
                q.append([con[i][0],con[i][1]])
    if(check):#해피를 출력 못했으면
        print('sad')#못가는 거니까 슬퍼
