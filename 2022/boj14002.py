import sys

n=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]

dp=[[1,[]] for _ in range(1001)]
ans=0
for i in range(n):
    dp[i][1].append(nums[i])

for i in range(n):
    for j in range(i+1,n):
        if(nums[i]<nums[j] and dp[j][0]<dp[i][0]+1):
            dp[j][0]=dp[i][0]+1
            dp[j][1]=dp[i][1].copy()
            dp[j][1].append(nums[j])
            if(dp[ans][0]<dp[j][0]):
                ans=j

print(dp[ans][0])
for i in dp[ans][1]:
    print(i,end=" ")
print()