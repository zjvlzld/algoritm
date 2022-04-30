#include<stdio.h>

int num[1002][1002];
int dp[1002][1002];

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);

    for(int i=1;i<=a;i++)
    {
        for(int j=1;j<b+1;j++)
        {
            scanf("%d",&num[i][j]);
        }
    }

    for(int i=1;i<=a;i++)
    {
        for(int j=1;j<=b;j++)
        {
            int add=0;
            if(add<dp[i-1][j-1])
            {
                add=dp[i-1][j-1];
            }
            if(add<dp[i][j-1])
            {
                add=dp[i][j-1];
            }
            if(add<dp[i-1][j])
            {
                add=dp[i-1][j];
            }
            dp[i][j]=add+num[i][j];
        }
    }
    printf("%d",dp[a][b]);
}