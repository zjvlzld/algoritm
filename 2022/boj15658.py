import sys

n=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]
cal=[int(x) for x in sys.stdin.readline().split(" ")]

ans1=-1000000001
ans2=1000000001
def solution(before,now,c):
    global ans1
    global ans2
    if(now==n):
        ans1=max(before,ans1)
        ans2=min(ans2,before)
        return
    if(c[0]>0):
        c[0]-=1
        solution(before+nums[now],now+1,c)
        c[0]+=1
    if(c[1]>0):
        c[1]-=1
        solution(before-nums[now],now+1,c)
        c[1]+=1
    if(c[2]>0):
        c[2]-=1
        solution(before*nums[now],now+1,c)
        c[2]+=1
    if(c[3]>0):
        c[3]-=1
        solution(int(before/nums[now]),now+1,c)
        c[3]+=1
solution(nums[0],1,cal)
print(ans1)
print(ans2)