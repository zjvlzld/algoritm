#include<stdio.h>
// 최대한 많은 단체 후에 사전순임
int main()
{
  long long group[200001][2];
  long long ans[200000];
  long long count=0;
  long long n;
  scanf("%lld",&n);
  n++;
  for(long long i=1;i<n;i++)
  {
    scanf("%lld %lld",&group[i][0],&group[i][1] );
  }
  ans[count]=1;
  count++;
  for(long long i=2;i<n;i++)
  {
    if(group[i][0]>group[ans[count-1]][1])
    {
      ans[count]=i;
      count++;
    }
  }
  printf("%lld\n",count);
  for(long long i=0;i<count;i++)
  {
    printf("%lld ",ans[i]);
  }
  return 0;
}
