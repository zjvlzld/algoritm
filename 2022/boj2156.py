import sys
n=int(sys.stdin.readline())

dp=[0,0,0]

for i in range(6):
    before=dp.copy()
    get=int(sys.stdin.readline())
    dp[0]=max(before)
    dp[1]=before[0]+get
    dp[2]=before[1]+get

print(max(dp))