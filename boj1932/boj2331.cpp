#include<stdio.h>

int num[300000];

int main()
{
   int first,p,i=1;
   scanf("%d %d",&first,&p);
   while(!num[first])
   {
       int t=0;
       int add=0;
       num[first]=i;
       while(first!=0)
       {
           int digit=first%10;
           first/=10;
           int temp=1;
           for(int i=0;i<p;i++)
           {
               temp*=digit;
           }
           add+=temp;
       }
       first=add;
       i++;
   }
   printf("%d",num[first]-1);
}