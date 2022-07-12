T=int(input())

for test in range(1,T+1):
    n=int(input())
    m=[]
    for _ in range(n):
        m.append([int(x) for x in input().strip().split(' ')])
    print(f"#{test}")
    for i in range(n):
        for j in range(n):
            print(m[n-1-j][i],end="")
        print(' ',end="")
        for j in range(n):
            print(m[n-1-i][n-1-j],end="")
        print(' ',end="")
        for j in range(n):
            print(m[j][n-1-i],end="")
        print()
