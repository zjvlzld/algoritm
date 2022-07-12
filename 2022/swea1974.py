T=int(input())
for test in range(1,T+1):
    ans=1
    m=[]
    check=[0 for _ in range(9)]
    for _ in range(9):
        m.append([int(x) for x in input().strip().split(' ')])
    for i in range(9):
        check=[0 for _ in range(9)]
        for j in range(9):
            check[m[i][j]-1]+=1
        for j in range(9):
            if(check[j]!=1):
                ans=0
                break
        if(ans==0):
            break
        check=[0,0,0,0,0,0,0,0,0]
        for j in range(9):
            check[m[j][i]-1]+=1
        for j in range(9):
            if(check[j]!=1):
                ans=0
                break
        if(ans==0):
            break
    if(ans==0):
        print(f"#{test} {ans}")
        continue
    for i in range(3):
        for j in range(3):
            check=[0,0,0,0,0,0,0,0,0]
            for k in range(3):
                for l in range(3):
                    check[m[i*3+k][j*3+l]-1]+=1
            
            for k in range(9):
                if(check[k]!=1):
                    ans=0
                    break
            if(ans==0):
                break
        if(ans==0):
            break
    print(f"#{test} {ans}")

