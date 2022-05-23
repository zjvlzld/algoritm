T = int(input())
ans=""
for case in range(1,T+1):
    a,b=map(int,input().split())
    if(a>9 or b>9):
        ans=ans+"#"+str(case)+" -1\n"
    else:
        ans=ans+"#"+str(case)+" "+str(a*b)+"\n"

print(ans)