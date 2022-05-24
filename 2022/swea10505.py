
T = int(input())

for case in range(1,T+1):
    n=int(input())
    nums=[int(x) for x in input().split()]
    a=sum(nums)/len(nums)
    ans=0
    for i in nums:
        if a>=i:
            ans+=1
    print(f"#{case} {ans}")