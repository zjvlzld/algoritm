import sys

n=int(sys.stdin.readline())
ans=1
checker=False
for i in range(2,n+1):
    ans=(ans*i)
    while True:
        if(ans%10==0):
            ans//=10
        else:
            break
    if(ans>1000000000000):
        checker=True
    ans=ans%1000000000000

if checker:
    for i in range(4,-1,-1):
        print(ans%10**(i+1)//10**i,end="")
else:
    print(ans%100000)

