import sys
a,b=map(int,input().split())
nums=[int(x) for x in input().split()]

ans=0

def solution(now):
    global ans
    if(len(now)==a):
        if(sum(now)!=0):
            t=0
            for i in range(a):
                t+=nums[i]*now[i]
            if t==b:
                ans+=1
        return
    now.append(1)
    solution(now)
    now.pop()
    now.append(0)
    solution(now)
    now.pop()
    return

solution([])
print(ans)