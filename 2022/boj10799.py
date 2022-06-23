get=input()
ans=0
stack=0
for i in range(len(get)):
    if get[i]=="(":
        stack+=1
    else:
        if(get[i-1]=="("):
            ans+=(stack-1)
            stack-=1
        else:
            stack-=1
            ans+=1
print(ans)
    