import sys

n1=sys.stdin.readline().rstrip()
n2=sys.stdin.readline().rstrip()
dp=[[0 for _ in range(len(n2)+1)]for _ in range(len(n1)+1)]

ans=0
for i in range(1,len(n1)+1):
    for j in range(1,len(n2)+1):
        if n1[i-1]==n2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            ans=max(ans,dp[i][j])
if(ans==1):
    print(0)
    exit()
print(ans)