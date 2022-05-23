T = int(input())

for case in range(1,T+1):
    a,b,c=map(int,input().split())
    ans=0
    for i in range(c):
        ans+=a*(1+i*b/100)
    if(ans==ans//1):
        ans=ans//1
        ans=int(ans)
    print(f"#{case} {ans}")