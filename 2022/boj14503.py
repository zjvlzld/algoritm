import sys

Y,X=map(int,sys.stdin.readline().split(" "))

s_y,s_x,direction=map(int,sys.stdin.readline().split(" "))

m=[]
for _ in range(Y):
    m.append([int(x) for x in sys.stdin.readline().split(" ")])
ans=0
while True:
    if m[s_y][s_x]==0:
        ans+=1
        m[s_y][s_x]=2
    count=0
    for _ in range(4):
        if(direction==0):
            direction=3
            if(s_x-1>=0):
                if(m[s_y][s_x-1]==0):
                    s_x=s_x-1
                    break
            count+=1

        elif(direction==1):
            direction=0
            if(s_y-1>=0):
                if(m[s_y-1][s_x]==0):
                    s_y=s_y-1
                    break
            count+=1
        elif(direction==2):
            direction=1
            if(s_x+1<X):
                if(m[s_y][s_x+1]==0):
                    s_x=s_x+1
                    break
            count+=1

        else:
            direction=2
            if(s_y+1<Y):
                if(m[s_y+1][s_x]==0):
                    s_y=s_y+1
                    break
            count+=1
    if(count==4):
        if(direction==0):
            if(s_y+1>=Y or m[s_y+1][s_x]==1):
                break
            else:
                s_y+=1
        if(direction==1):
            if(s_x-1<0 or m[s_y][s_x-1]==1):
                break
            else:
                s_x-=1
        if(direction==2):
            if(s_y-1<0 or m[s_y-1][s_x]==1):
                break
            else:
                s_y-=1
        if(direction==3):
            if(s_x+1>=X or m[s_y][s_x+1]==1):
                break
            else:
                s_x+=1

print(ans)