from typing import Final


T = int(input())

for case in range(1,T+1):
    N=int(input())
    pan=[]
    for _ in range(N):
        pan.append(input())
    finalCheck=True
    for i in range(N):
        out=False
        for j in range(N):
            if pan[i][j]=='o':
                check=True
                for c in range(5):
                    if not(i+c<N and pan[i+c][j]=='o'):
                        check=False
                        break
                if(check):
                    out=True
                    break

                check=True
                for c in range(5):
                    if not(j+c<N and pan[i][j+c]=='o'):
                        check=False
                        break
                if(check):
                    out=True
                    break

                check=True
                for c in range(5):
                    if not(j+c<N and i+c<N and pan[i+c][j+c]=='o'):
                        check=False
                        break
                if(check):
                    out=True
                    break
                
                check=True
                for c in range(5):
                    if not(j-c>=0 and i+c<N and pan[i+c][j-c]=='o'):
                        check=False
                        break
                if(check):
                    out=True
                    break
        if(out):
            print(f"#{case} YES")
            finalCheck=False
            break
    if(finalCheck):
        print(f"#{case} NO")

    
