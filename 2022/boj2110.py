N,C=map(int,input().split(' '))
h=[]
ans=0
def checker(length):
    global ans
    now=h[0]
    count=1
    for i in range(1,N):
        if(h[i]>=now+length):
            now=h[i]
            count+=1
    return count

for _ in range(N):
    h.append(int(input()))
h.sort()
l=1
r=h[-1]-h[0]
while(l<r):
    mid=(l+r)//2
    if(checker(mid)>=C):
        l=mid+1
    else:
        r=mid
if(C!=2):
    print(r-1)
else:
    print(r)