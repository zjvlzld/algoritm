import sys

for _ in range(3):
    pan=[]
    plate=[0,0,0,0,0,0]
    direction=[[1,2,3,4],[5,2,0,4],[1,5,3,0],[0,2,5,4],[1,0,3,5],[3,4,1,2]]
    dx=[-1,0,1,0]
    dy=[0,-1,0,1]
    for _ in range(6):
        pan.append([int(x) for x in sys.stdin.readline().split(" ")])
    x=y=-1
    for i in range(6):
        for j in range(6):
          if pan[i][j]==1:
            y=i
            x=j
            break
        if(x!=-1 or y!=-1):
            break
    q=[]
    q.append([y,x,0])
    plate[0]=1
    pan[y][x]=2
    while(len(q)!=0):
        now=q[0]
        q.pop(0)
        for i in range(4):
            if(0<=now[0]+dy[i]<6 and 0<now[1]+dx[i]<6 and pan[ now[0]+dy[i] ][ now[1]+dx[i] ]==1):
                q.append([now[0]+dy[i],now[1]+dx[i],direction[now[2]][i]])
                pan[now[0]+dy[i]][now[1]+dx[i]]=2
                plate[direction[now[2]][i]]=1
                print(now[2],direction[now[2]][i],i)
    print(plate)
    print()
    for i in pan:
        print(i)
    if(sum(plate)==6):
        print('yes')
    else:
        print('no')