#define _CRT_SECURE_NO_WARNINGS
#include<iostream>

using namespace std;
int cost[18][2];
int endDay;

int get(int now)
{
	if (now > endDay)
	{
		return 0;
	}
	int a = get(now + 1);
	int b = 0;
	if (now + cost[now][0] <= endDay + 1)
	{
		b = cost[now][1] + get(now + cost[now][0]);
	}
	if (a > b)
	{
		return a;
	}
	return b;
}



int main()
{
	scanf("%d", &endDay);
	for (int i = 1; i < endDay + 1; i++)
	{
		scanf("%d %d", &cost[i][0], &cost[i][1]);

	}
	printf("%d", get(1));
	return 0;
}