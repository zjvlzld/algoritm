T = int(input())
ans=""
for case in range(1,T+1):
    a,b=map(int,input().split())
    ans=ans+"#"+str(case)+" "+str((a+b)%24)+"\n"

print(ans)