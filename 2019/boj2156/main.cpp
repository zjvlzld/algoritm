#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int dp[10001][3];

int main() 
{
	int N;
	scanf("%d",&N);
	int get;
	scanf("%d",&get);
	dp[0][0]=0;
	dp[0][1]=get;
	dp[0][2]=0;
	for(int i=1;i<N;i++)
	{
		scanf("%d",&get);
		dp[i][0]=get+dp[i-1][1];
		dp[i][1]=get+dp[i-1][2];
		dp[i][2]=dp[i-1][0];
		if(dp[i][2]<dp[i-1][1])
		{
			dp[i][2]=dp[i-1][1];
		}
		if(dp[i][2]<dp[i-1][2])
		{
			dp[i][2]=dp[i-1][2];
		}
	}	
	int ans=0;
	for(int i=0;i<3;i++)
	{
		if(dp[N-1][i]>ans)
		{
			ans=dp[N-1][i];
		}
	}
	printf("%d",ans);
	return 0;
}
