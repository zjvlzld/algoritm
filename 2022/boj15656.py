a,b=map(int, input().split(" "))
nums=[int(x) for x in input().split(" ")]
nums.sort()

def solution(now,length,nums):
    if(len(now)==length):
        for i in now:
            print(i,end=" ")
        print()
        return
    for i in range(len(nums)):
        now.append(nums[i])
        solution(now,length,nums)
        now.pop()

solution([],b,nums)