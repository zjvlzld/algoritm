import sys
ans=0
while True:
    ans+=1
    t=int(sys.stdin.readline())
    if(t==0):
        exit()
    pan=[[0 for _ in range(9)]for _ in range(9)]
    
    tile=[[0 for i in range(10)]for _ in range(10)]
 
    for _ in range(t):
        n1,p1,n2,p2=sys.stdin.readline().split(" ")
        n1=int(n1)
        n2=int(n2)
        tile[n1][n2]=1
        tile[n2][n1]=1
        pan[ord(p1[0])-ord('A')][int(p1[1])-1]=n1
        pan[ord(p2[0])-ord('A')][int(p2[1])-1]=n2
    get=sys.stdin.readline().rstrip().split(" ")
    #print(get)
    for i in range(9):
        pan[ord(get[i][0])-ord('A')][int(get[i][1])-1]=i+1
    
    count=0
    for i in pan:
        for j in i:
            if j==0:
                count+=1

    isPrinted=False

    def solution(c):
        #print(c)
        global isPrinted
        if isPrinted:
            return
        if(c==0):
            isPrinted=True
            print('Puzzle',ans)
            for i in pan:
                for j in i:
                    print(j,end="")
                print()
            return
        #print('asdf')
        for i in range(9):
            for j in range(9):
                if(pan[i][j]==0):
                    #print(i,j)
                    check=[0,0,0,0,0,0,0,0,0,0]
                    for l in range(9):
                        check[pan[i][l]]=1
                        check[pan[l][j]]=1
                    for l in range(3):
                        for k in range(3):
                            check[pan[(i//3)*3+l][(j//3)*3+k]]=1
                    #print(check)
                    for l in range(1,10):
                        if(check[l]==0):
                            pan[i][j]=l
                #            print(count,i,j,pan[i][j],'test',tile[l])
                            
                            for next in range(1,10):
                                if(tile[l][next]==0):
                                    if(j+1<9 and pan[i][j+1]==0):
                                        check2=[0,0,0,0,0,0,0,0,0,0]
                                        for l2 in range(9):
                                            check2[pan[i][l2]]=1
                                            check2[pan[l2][j+1]]=1
                                        for l2 in range(3):
                                            for k2 in range(3):
                                                check2[pan[(i//3)*3+l2][((j+1)//3)*3+k2]]=1
                                        if(check2[next]==0):
                                            tile[l][next]=1
                                            tile[next][l]=1
                                            pan[i][j+1]=next
                                            solution(c-2)
                                            pan[i][j+1]=0
                                            tile[l][next]=0
                                            tile[next][l]=0
                                    if(i+1<9 and pan[i+1][j]==0):
                                        check2=[0,0,0,0,0,0,0,0,0,0]
                                        for l2 in range(9):
                                            check2[pan[i+1][l2]]=1
                                            check2[pan[l2][j]]=1
                                        for l2 in range(3):
                                            for k2 in range(3):
                                                check2[pan[((i+1)//3)*3+l2][((j)//3)*3+k2]]=1
                                        if(check2[next]==0):
                                            tile[l][next]=1
                                            tile[next][l]=1
                                            pan[i+1][j]=next
                                            solution(c-2)
                                            pan[i+1][j]=0
                                            tile[l][next]=0
                                            tile[next][l]=0
                            pan[i][j]=0
                    #print('end',i,j)
                    return
    
    
    solution(count)
#    print('end?')
    
    
    
    
    
    
