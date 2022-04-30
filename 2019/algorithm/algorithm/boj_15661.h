#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>

using namespace std;

int abs(int i)
{
	if (i < 0)
	{
		return i*-1;
	}
	return i;
}
int getSq(int n)
{
	int r = 1;
	for (int i = 0; i < n; i++)
	{
		r=r * 2;
	}
	return r;
}
int main()
{
	int nums;
	int cost[21][21];
	int ans = 100000;

	scanf("%d", &nums);
	for (int i = 0; i < nums; i++)
	{
		for (int j = 0; j < nums; j++)
		{
			scanf("%d", &cost[i][j]);
		}
	}
	for (int i = 0; i < getSq(nums); i++)
	{
		int t1 = 0, t2 = 0;
		bool check[21] = {false};
		for (int p = 0; p < nums; p++)
		{
			if ((i & (1 << p)) > 0)
			{
				check[p] = true;
			}
		}
		for (int a = 0; a < nums; a++)
		{
			for (int b = 0; b < nums; b++)
			{
				if (check[a] && check[b])
				{
					t1 = t1 + cost[a][b];
				}
				if (!(check[a] || check[b]))
				{
					t2 = t2 + cost[a][b];
				}
			}
		}
		if (abs(t1 - t2)<ans)
		{
			ans = abs(t1 - t2);
		}
	}
	printf("%d", ans);
}