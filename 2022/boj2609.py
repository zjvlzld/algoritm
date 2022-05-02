a,b=map(int,input().split())

def gcd(a,b):
    if(a<b):
        return gcd(b,a)
    if(a%b==0):
        return b

    return gcd(b,a%b)

print(gcd(a,b))
print(a*b//gcd(a,b))