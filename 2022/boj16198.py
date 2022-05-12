import sys

n=int(sys.stdin.readline())

nums=[int(x) for x in sys.stdin.readline().split(" ")]
visit=[0 for _ in range(n)]

ans=0


def solution(t,count):
    global ans
    ans=max(ans,t)
    if(count==n-2):
        return
    for i in range(1,n-1):
        if(visit[i]==0):
            add=1
            for j in range(i-1,-1,-1):
                if(visit[j]==0):
                    add*=nums[j]
                    break
            for j in range(i+1,n):
                if(visit[j]==0):
                    add*=nums[j]
                    break
            visit[i]=1
            solution(t+add,count+1)
            visit[i]=0
solution(0,0)
print(ans)    