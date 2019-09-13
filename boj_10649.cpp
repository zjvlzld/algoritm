#include<stdio.h>
#include<algorithm>
using namespace std;
int check[10];
int num[10];
int nums[10];
int stack[10];
bool check2[100000000];
int a,b;

void print(int now,int big,int checking)
{
    if(now==b)
    {
       // printf("%d    | ",checking);
        /*if(check2[checking])
        {
        //    printf("\n");
            return ;
        }*/
        for(int i=1;i<b+1;i++)
        {
            printf("%d ",nums[stack[i]]);
        }
        printf("\n");
        //check2[checking]=true;
        return;
    }
    for(int i=big+1;i<a+1;i++)
    {
        if(check[i]==0)
        {
            //check[i]=1;
            stack[now+1]=i;
            print(now+1,i-1,0/*checking*10+num[i]*/);
            //check[i]=0;
        }
    }
}

int main()
{
    scanf("%d %d",&a,&b);
    for(int i=1;i<a+1;i++)
    {
        scanf("%d",&num[i]);
    }
    sort(num+1,num+a+1);
    int t=1;
    for(int i=1;i<a+1;i++)
    {
        if(num[i]!=num[i-1])
        {
            nums[t]=num[i];
            t++;
        }
    }
    a=t-1;
/*    for(int i=1;i<a+1;i++)
    {
     //   printf("%d",nums[i]);
    }
   // printf("\n");
    for(int i=1;i<a+1;i++)
    {
//        printf("%d",num[i]);
    }
    //printf("\n");*/
    print(0,0,0);
}