T = int(input())
ans=""

def gcd(a,b):
    if(a<b):
        a,b=b,a
    if(b==0):
        return a
    return gcd(a%b,b)
for case in range(1,T+1):
    get=input()
    a,b=1,1

    for d in get:
        if(d=='L'):
            b=a+b
        if(d=='R'):
            a=a+b
        divi=gcd(a,b)
        a=a//divi
        b=b//divi
    ans+="#"+str(case)+ " "+str(a)+" "+str(b)+'\n'
print(ans)