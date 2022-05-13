import sys

n1=sys.stdin.readline().rstrip()
n2=sys.stdin.readline().rstrip()

dp=[[[0,""] for _ in range(len(n2)+1)]for _ in range(len(n1)+1)]

for i in range(1,len(n1)+1):
    for j in range(1,len(n2)+1):

        dp[i][j]=dp[i-1][j][:]
        if(dp[i][j][0]<dp[i][j-1][0]):
            dp[i][j]=dp[i][j-1][:]
        
        if(n1[i-1]==n2[j-1]):
            dp[i][j]=dp[i-1][j-1][:]
            dp[i][j][0]+=1
            dp[i][j][1]+=n1[i-1]
print(dp[len(n1)][len(n2)][0])
if(dp[len(n1)][len(n2)][0]==0):
    exit()
print(dp[len(n1)][len(n2)][1])