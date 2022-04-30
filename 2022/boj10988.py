get=input()

ans=1
for i in range(len(get)//2):
    if(get[i]!=get[len(get)-1-i]):
        ans=0
        break

print(ans)