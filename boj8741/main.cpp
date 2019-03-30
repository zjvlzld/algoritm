#include <cstdio>

int main() 
{
	int get;
	scanf("%d",&get);
	for(int i=0;i<get;i++)
	{
		printf("1");
	}
	for(int i=0;i<get-1;i++)
	{
		printf("0");
	}
	return 0;
}
