import sys


pan=[]

for _ in range(9):
    pan.append([int(x) for x in sys.stdin.readline().split(" ")])

z=[]
count=0
for i in pan:
    for j in i:
        if(j==0):
            count+=1
                
def solution(c):
    if(c==0):
        for i in pan:
            for j in i:
                print(j,end=" ")
            print()
        exit()
        
    for i in range(9):
        for j in range(9):
            if(pan[i][j]==0):
                check=[0,0,0,0,0,0,0,0,0,0,0]
                for l in range(9):
                    check[ pan[i][l]]=1
                    check[ pan[l][j]]=1
                for t1 in range(3):
                    for t2 in range(3):
                        check[pan[(i//3)*3+t1][(j//3)*3+t2]]=1
                for l in range(1,10):
                    if(check[l]==0):
                        pan[i][j]=l
                        solution(c-1)
                        pan[i][j]=0
    


solution(count)