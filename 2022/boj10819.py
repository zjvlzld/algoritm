T=int(input())
ans=0
used=[0 for _ in range(T)]
nums=[int(x) for x in input().split(" ")]
def solution(now,count):
    global ans
    if(count==T):
        temp=0
        for i in range(T-1):
            temp+=abs(now[i]-now[i+1])
        if(temp>ans):
            ans=temp

    for i in range(T):
        if(used[i]==0):
            used[i]=1
            now.append(nums[i])
            solution(now,count+1)
            used[i]=0
            now.pop()

solution([],0)
print(ans)