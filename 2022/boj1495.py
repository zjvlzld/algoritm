import sys
import copy
n,s,m=map(int,sys.stdin.readline().split(" "))

nums=[int(x) for x in sys.stdin.readline().split(" ")]

dp=[0 for _ in range(m+1)]
dp[s]=1
count=1
for i in nums:
    temp=dp[:]
    for j in range(m+1):
        if(temp[j]==1):
            dp[j]=0
            count-=1
            if(j-i>=0):
                dp[j-i]=1
                count+=1
            if(j+i<=m):
                dp[j+i]=1
                count+=1
    if(count==0):
        print(-1)
        exit()

for i in range(m,-1,-1):
    if(dp[i]==1):
        print(i)
        exit()
print(-1)