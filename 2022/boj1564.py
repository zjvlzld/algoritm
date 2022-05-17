import sys

n=int(sys.stdin.readline())
ans=1
checker=True
checkNums=1
for i in range(2,n+1):
    if(checker):
        checkNums*=i
        if(checkNums>10000000000)
    ans=(ans*i)
    while True:
        if(ans%10==0):
            ans//=10
        else:
            break
    ans=ans%100000
print(ans)
for i in range(4,-1,-1):
    print(ans%10**(i+1)//10**i,end="")
print()

