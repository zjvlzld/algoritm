T = int(input())
p=""
for case in range(1,T+1):
    a,b,c=map(int,input().split())

    if(b+c>a):
        p+=(f"#{case} {min(b,c)} {b+c-a}\n")
    else:
        p+=(f"#{case} {min(b,c)} 0\n")
print(p)