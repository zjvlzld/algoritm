T=int(input())
for _ in range(T):
    nums=[int(x) for x in input().split(' ')]

    average=sum(nums[1:])//nums[0]

    s=0
    for i in nums[1:]:
        if i>average:
            s+=1
    print('%.3f'%round(s/nums[0]*100,3)+'%')