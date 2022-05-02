a,b=map(int, input().split(" "))
nums=[int(x) for x in input().split(" ")]
nums.sort()

def solution(now,length,nums,s):
    if(len(now)==length):
        for i in now:
            print(i,end=" ")
        print()
        return
    for i in range(s,len(nums)):
        now.append(nums[i])
        solution(now,length,nums,i)
        now.pop()

solution([],b,nums,0)