import sys

n,m,nowY,nowX,o=map(int,sys.stdin.readline().split(" "))

pan=[]

dice=[0,0,0,0,0,0]
for _ in range(n):
    pan.append([int(x) for x in sys.stdin.readline().split(" ")])

order=[int(x) for x in sys.stdin.readline().split(" ")]

for i in order:
    if(i==2):
        if(nowX-1>=0):
            if(pan[nowY][nowX-1]==0):
                pan[nowY][nowX-1]=dice[3]
                dice[3]=dice[5]
                dice[5]=dice[2]
                dice[2]=dice[0]
                dice[0]=pan[nowY][nowX-1]       
            else:
                t=pan[nowY][nowX-1]
                pan[nowY][nowX-1]=0
                dice[3]=dice[5]
                dice[5]=dice[2]
                dice[2]=dice[0]
                dice[0]=t
            nowX-=1
            print(dice[5])
    if(i==1): 
        if(nowX+1<=m-1):
            if(pan[nowY][nowX+1]==0):
                pan[nowY][nowX+1]=dice[2]
                dice[2]=dice[5]
                dice[5]=dice[3]
                dice[3]=dice[0]
                dice[0]=pan[nowY][nowX+1]
            else:
                t=pan[nowY][nowX+1]
                pan[nowY][nowX+1]=0
                dice[2]=dice[5]
                dice[5]=dice[3]
                dice[3]=dice[0]
                dice[0]=t
            nowX+=1
            print(dice[5])

    if(i==3):
        if(nowY-1>=0):
            if(pan[nowY-1][nowX]==0):
                pan[nowY-1][nowX]=dice[1]
                dice[1]=dice[5]
                dice[5]=dice[4]
                dice[4]=dice[0]
                dice[0]=pan[nowY-1][nowX]
            else:
                t=pan[nowY-1][nowX]
                pan[nowY-1][nowX]=0
                dice[1]=dice[5]
                dice[5]=dice[4]
                dice[4]=dice[0]
                dice[0]=t
            nowY-=1
            print(dice[5])

    if(i==4):       
        if(nowY+1<=n-1):
            if(pan[nowY+1][nowX]==0):
                pan[nowY+1][nowX]=dice[4]
                dice[4]=dice[5]
                dice[5]=dice[1]
                dice[1]=dice[0]
                dice[0]=pan[nowY+1][nowX]
            else:
                t=pan[nowY+1][nowX]
                pan[nowY+1][nowX]=0
                dice[4]=dice[5]
                dice[5]=dice[1]
                dice[1]=dice[0]
                dice[0]=t
            nowY+=1
            print(dice[5])
