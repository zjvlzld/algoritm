#include <stdio.h>

int a,b;
int check[10];
int print_num[10];

void print_n(int now)
{
    if(now==b)
    {
        for(int i=1;i<b+1;i++)
        {
            printf("%d ",print_num[i]);
        }
        printf("\n");
        return ;
    }
    for(int i=1;i<a+1;i++)
    {
        if(check[i]==0)
        {
            check[i]==1;
            print_num[now+1]=i;
            print_n(now+1);
        }
    }
}


int main()
{
    scanf("%d %d",&a,&b);
    print_n(0);
}