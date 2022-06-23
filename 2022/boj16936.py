n=int(input())
nums=[int(x) for x in input().split(' ')]
check=set()
ans=[nums[0]]
check.add(nums[0])
def solution(now):
    global ans
    if(now*2 in nums and now*2 not in check):
        ans.append(now*2)
        check.add(now*2)
        solution(now*2)
    if(now%3==0 and now//3 in nums and now//3 not in check):
        ans.append(now//3)
        check.add(now//3)
        solution(now//3)
    if(now//2 in nums and now//2 not in check):
        ans=[now//2]+ans
        check.add(now//2)
        solution(now//2)
    if(now*3 in nums and now*3 not in check):
        ans=[now*3]+ans
        check.add(now*3)
        solution(now*3)
solution(nums[0])
for i in ans:
    print(i,end=" ")