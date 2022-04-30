#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int tri[502][502];
int dp[502][502];
int main() 
{
	int N;
	scanf("%d",&N);
	for(int i=1;i<N+1;i++)
	{
		for(int j=1;j<i+1;j++)
		{
			scanf("%d",&tri[i][j]);
			if(dp[i][j]<tri[i][j]+dp[i-1][j])
			{
				dp[i][j]=tri[i][j]+dp[i-1][j];
			}
			if(dp[i][j]<tri[i][j]+dp[i-1][j-1])
			{
				dp[i][j]=tri[i][j]+dp[i-1][j-1];
			}
		}	
	}
	int ans=0;
	for(int i=1;i<N+1;i++)
	{
		if(ans<dp[N][i])
		{
			ans=dp[N][i];
		}
	}
	printf("%d",ans);
	return 0;
}
