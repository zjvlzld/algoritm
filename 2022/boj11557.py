T=int(input())
for _ in range(T):
    n=int(input())
    university=[["",0] for _ in range(n)]
    for i in range(n):
        a,b=input().split(" ")
        university[i]=[a,int(b)]
    
    university.sort(key=lambda x : -x[1])
    print(university[0][0])
