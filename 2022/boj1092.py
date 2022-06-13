nc=int(input())

crane=[int(x) for x in input().split(' ')]
cranePoint=[0 for _ in range(nc)]
ns=int(input())

done=[0 for _ in range(ns)]
stuff=[int(x) for x in input().split(' ')]
if(max(crane)<max(stuff)):
    print(-1)
    exit()
crane.sort(reverse=True)
stuff.sort(reverse=True)
ans=0
count=0
while count<ns:
    ans+=1
    for i in range(nc):
        if(count>=ns):
            break
        while cranePoint[i]<ns and (done[cranePoint[i]]==1 or crane[i]<stuff[cranePoint[i]]):
            cranePoint[i]+=1
        if(cranePoint[i]>=ns):
            break
        done[cranePoint[i]]=1
        count+=1
        cranePoint[i]+=1
print(ans)
        
