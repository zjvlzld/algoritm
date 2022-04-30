#include<cstdio>

int main()
{
	long long ans = 0;
	int num=0;
	char get;
	int len = 0;
	scanf("%d", &len);
	for (int i = 0; i <= len; i++)
	{
		scanf("%c", &get);
		if ((int)get > 47 && (int)get < 58)
		{
			num=num*10+(int)get - 48;
		}
		else
		{
			ans += num;
			num = 0;
		}
	}
	ans += num;
	num = 0;
	printf("%lld", ans);
}