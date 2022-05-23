T = int(input())
ans=""
for case in range(1,T+1):
    a,b,c=map(int,input().split())

    if(b>c):
        ans+="#"+str(case)+" Possible\n"
    else:
        if(999*a>=1000*a*c/100-a*b/100):
            ans+="#"+str(case)+" Possible\n"
        else:
            ans+="#"+str(case)+" Broken\n"
print(ans)