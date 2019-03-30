#include <cstdio>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	int num;
	scanf("%d",&num);
	for(int i=1;i<num+1;i++)
	{
		int y=0;
		int get;
		for(int j=1;j<6;j++)
		{
			scanf("%d",&get);
			y+=(get==j);
		}
		for(int j=1;j<6;j++)
		{
			scanf("%d",&get);
			y+=(get==j);
		}
		if(y==10)
		{
			printf("%d",i);
		}
	}
	return 0;
}
