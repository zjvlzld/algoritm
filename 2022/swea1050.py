from tkinter import FALSE


T = int(input())
dp=[0 for _ in range(1001)]
for i in range(1,1001):
    t=str(i)
    check=False
    for j in range(len(t)//2+1):
        if(t[j] != t[len(t)-1-j]):
            check=True
            break
    if(check):
        continue
    sq=0
    if(i**(1/2)==int(i**(1/2))):
        sq=int(i**(1/2))
        t=str(sq)
        check=False
        for j in range(len(t)//2+1):
            if(t[j] != t[len(t)-1-j]):
                check=True
                break
        if(check):
            continue
    else:
        continue
    dp[i]=1
for case in range(1,T+1):
    a,b=map(int,input().split())
    print(f"#{case} {sum(dp[a:b+1])}")

