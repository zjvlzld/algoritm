#include <stdio.h>

int dp[1000][10];

int main()
{
    int t=0;
    for(int i=0;i<10;i++)
    {
        dp[0][i]=1;
    }
    scanf("%d",&t);
    for(int i=1;i<t;i++)
    {
        for(int j=0;j<10;j++)
        {
            for(int k=0;k<=j;k++)
            {
                dp[i][j]+=dp[i-1][k];
            }
            dp[i][j]%=10007;
        }
    }
    int ans=0;
    for(int i=0;i<10;i++)
    {
        ans+=dp[t-1][i];
    }
    ans%=10007;
    printf("%d",ans);
}