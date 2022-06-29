get=input()
n=int(input())
ans=0
for _ in range(n):
    get2=input()
    if(get in get2):
        ans+=1
print(ans)