nums=[int(x) for x in input().split(' ')]
ans=[1,sum(nums)]
for i in range(2,6):
    nums=[int(x) for x in input().split(' ')]
    if sum(nums)>ans[1]:
        ans=[i,sum(nums)]
print(ans[0],ans[1])