m=[]
for _ in range(9):
    m.append([int(x) for x in input().split(' ')])
check=[0 for _ in range(9)]
for i in range(9):
    for j in range(9):
        check[m[j][i]-1]=1
    for j in range(9):
        if(check[j]!=1):
            ans=0
            print(i)
            break        