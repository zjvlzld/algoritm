T = int(input())

ans=""

for case in range(1,T+1):
    a,b,c,d=map(int,input().split())

    t=min(b,d)-max(a,c)
    if(t<0):
        ans=ans+"#"+str(case)+" 0\n"
    else:
        ans=ans+"#"+str(case)+" "+str(t)+"\n"
        
print(ans)