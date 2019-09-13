#include <cstdio>

int dp[100000][101];
int coin[100][2];

int main()
{
  int cost;
  scanf("%d",&cost);
  int num;
  scanf("%d",&num );
  for(int i=0;i<num;i++)
  {
    scanf("%d %d",&coin[i][0],&coin[i][1]);
  }
  for(int i=0;i<cost;i++)
  {
    for(int j=0;j<num;j++)
    {
      if(i>=coin[j][0])
      {
        
      }
    }
  }
}
