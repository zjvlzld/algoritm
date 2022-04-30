#include <cstdio>
//boj11052
//https://www.acmicpc.net/problem/11052
int num[1001];
int dp[1001];
int main()
{
  int get;
  scanf("%d",&get );
  for(int i=1;i<get+1;i++)
  {
    scanf("%d",&num[i] );
  }
  for(int i=1;i<get+1;i++)
  {
    for(int j=1;j<i+1;j++)
    {
      int temp=dp[i-j]+num[j];
      if(temp>dp[i])
      {
        dp[i]=temp;
      }
    }
  }
  printf("%d\n",dp[get]);
}
