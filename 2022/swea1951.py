T=int(input())

for test in range(1,T+1):
    ans=0
    a,b=map(int,input().split(' '))
    nums1=[int(x) for x in input().split(' ')]
    nums2=[int(x) for x in input().split(' ')]
    if(a>b):
        a,b=b,a
        t=nums1[:]
        nums1=nums2[:]
        nums2=t[:]
    for i in range(b-a+1):
        t=0
        for j in range(a):
            t+=nums2[i+j]*nums1[j]
        ans=max(t,ans)
    print(f"#{test} {ans}")