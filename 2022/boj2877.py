n=int(input())
def toBinary(n):
    ans=""
    while(n>0):
        ans=str(n%2)+ans
        n//=2
    return ans[1:]

for i in toBinary(n+1):
    if(i=='0'):
        print('4',end="")
    else:
        print('7',end="")
print()