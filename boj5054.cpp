#include <cstdio>

int main()
{
  int T;
  scanf("%d",&T);
  for(int test=0;test<T;test++)
  {
    int min=1000;
    int max=0;
    int get;
    int num;
    scanf("%d",&num);
    for(int i=0;i<num;i++)
    {
      scanf("%d",&get );
      if(get<min)
      {
        min=get;
      }
      if(get>max)
      {
        max=get;
      }
    }
    printf("%d\n",(max-min)*2);
  }

  return 0;
}
