import sys
n=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]

dp1=[-100000000 for _ in range(100001)]
dp2=[-100000000 for _ in range(100001)]

dp1[0]=nums[0]
dp2[0]=nums[0]

for i in range(1,n):
    dp1[i]=max(nums[i],dp1[i-1]+nums[i])
    dp2[i]=max(dp1[i-1],dp2[i-1]+nums[i])

print(max(max(dp1),max(dp2)))
