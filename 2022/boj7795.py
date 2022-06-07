T = int(input())

for _ in range(T):
    a,b=map(int,input().split(" "))
    numsA=[int(x) for x in input().split(" ")]
    numsB=[int(x) for x in input().split(" ")]
    numsA.sort()
    numsB.sort()
    ap=0
    bp=0
    ans=0
    while(ap<a):
        while(bp<b and numsA[ap]>numsB[bp]):
            bp+=1
        ans+=bp
        ap+=1
    print(ans)