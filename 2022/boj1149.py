from pickle import DUP
import sys
n=int(sys.stdin.readline())
dp=[int(x) for x in sys.stdin.readline().split(" ")]
for _ in range(n-1):
    before=dp.copy()
    get=[int(x) for x in sys.stdin.readline().split(" ")]
    dp[0]=min(before[1],before[2])+get[0]
    dp[1]=min(before[0],before[2])+get[1]
    dp[2]=min(before[0],before[1])+get[2]
print(min(dp))