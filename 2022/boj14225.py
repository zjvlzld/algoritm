import sys

dp=[0 for _ in range(2000001)]
t=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]
dp[0]=1


def solution(n,now):
    dp[now]=1

    if(n<t):
        solution(n+1,now)
        solution(n+1,now+nums[n])

solution(0,0)
for i in range(2000001):
    if(dp[i]==0):
        print(i)
        exit()