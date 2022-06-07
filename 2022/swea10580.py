T = int(input())

for case in range(1,T+1):
    n=int(input())
    line=[]
    for _ in range(n):
        line.append(list(map(int,input().split())))
    line.sort(key=lambda x : x[0])
    ans=0
    for i in range(n-1):
        for j in range(i+1,n):
            if line[i][1]>line[j][1]:
                ans+=1
    print(f"#{case} {ans}")