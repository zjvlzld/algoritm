a,b=map(int,input().split(" "))

if(a==b or b*100//a==99):
    print(-1)
    exit()
l=1
r=a

while(l<r):
    mid=(l+r)//2
    if (b+mid)*100//(a+mid)>b*100//a:
        r=mid
    else:
        l=mid+1
print(r)
