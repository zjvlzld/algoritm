#include<stdio.h>
#include<algorithm>


int num1[100001];
int num2[100001];

int search(int target, int l, int r)
{
    int mid= (l+r)/2;
    if(target==num1[mid])
    {
        return 1;
    }
    if(target==num1[r])
    {
        return 1;
    }
    if(mid==l)
    {
        return 0;
    }
    else if(target<num1[mid])
    {
        return search(target,l,mid-1);
    }
    else if(target>num1[mid])
    {
        return search(target,mid+1,r);        
    }
}


int main()
{
    int a,b,t;
    scanf("%d",&a);
    for(int i=0;i<a;i++)
    {
        scanf("%d",&num1[i]);
    }
    scanf("%d",&b);
    for(int i=0;i<b;i++)
    {
        scanf("%d",&num2[i]);
    }
    std::sort(num1,num1+a);
    for(int i=0;i<b;i++)
    {
        printf("%d\n",search(num2[i],0,a-1));
    }
    return 0;
}