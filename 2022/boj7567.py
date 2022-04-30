get=input()
ans=10
for i in range(1,len(get)):
    if(get[i]==get[i-1]):
        ans+=5
    else:
        ans+=10
print(ans)
