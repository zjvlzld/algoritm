get=int(input())

ans=0
for i in range(1,get+1):
    ans=ans+i*(get//i)
print (ans)