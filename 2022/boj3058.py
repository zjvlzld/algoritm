t=int(input())
for _ in range(t):
    nums=[int(x) for x in input().split(' ')]
    ans=0
    m=200
    for i in nums:
        if i%2==0:
            ans+=i
            m=min(m,i)
    print(ans,m)