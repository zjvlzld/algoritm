a,b=map(int, input().split(" "))
nums=[int(x) for x in input().split(" ")]
nums.sort()

def solution(now,length):
    if(len(now)==length):
        for i in now:
            print(i,end=" ")
        print()
        return
    for i in range(a):
        if not(nums[i] in now):
            now.append(nums[i])
            solution(now,length)
            now.pop()

solution([],b)