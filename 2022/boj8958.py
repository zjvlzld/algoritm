T=int(input())

for _ in range(T):
    get=input()
    
    ans=add=0
    for i in range(len(get)):
        if(get[i]=='O'):
            add+=1
            ans+=add
        else:
            add=0

    print(ans)