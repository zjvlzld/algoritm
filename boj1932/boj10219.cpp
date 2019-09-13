#include<stdio.h>

int main()
{
    int t;
    char c;

    scanf("%d",&t);
    scanf("%c",&c);
    for(int test=0;test<t;test++)
    {
        int a,b;
        char str[12][12];
        scanf("%d %d",&a,&b);
        scanf("%c",&c);
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                scanf("%c",&str[i][j]);
            }
            scanf("%c",&c);
        }
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                printf("%c",str[i][b-1-j]);
            }
            printf("\n",&c);
        }
    }
}
