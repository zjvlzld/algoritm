import sys

n=int(input())
gets=[]
for i in range(n):
    gets.append(input())

ans=""
for i in range(len(gets[0])):
    check=True
    p=gets[0][i]
    for j in range(1,n):
        if(p!=gets[j][i]):
            check=False
            break
    if(check):
        ans+=p
    else:
        ans+='?'
print(ans)