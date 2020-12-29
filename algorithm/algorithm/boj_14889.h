#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>

using namespace std;

int nums;
int cost[21][21];
bool check[21];
int ans=1000;
int abs(int i)
{
	if (i < 0)
	{
		return i*-1;
	}
	return i;
}
void team(int cnt,int now)
{
	int t1 = 0, t2 = 0;
	if (cnt == nums / 2)
	{
	
		for (int i = 0; i < nums; i++)
		{
			for (int j = 0; j < nums; j++)
			{
				if (check[i] && check[j])
				{
					t1 = t1 + cost[i][j] + cost[j][i];
				}
				if (!(check[i] || check[j]))
				{
					t2=t2+ cost[i][j] + cost[j][i];
				}
			}
		}
		if (ans > abs(t1 - t2))
		{
			ans = abs(t1 - t2);
		}
		return;
	}
	for (int i = now; i < nums; i++)
	{
		
		check[i] = true;
		team(cnt+1,i+1);
		check[i] = false;
		
	}
}

int main()
{
	scanf("%d", &nums);
	for (int i = 0; i < nums; i++)
	{
		for (int j = 0; j < nums; j++)
		{
			scanf("%d", &cost[i][j]);
		}
	}
	team(0,0);
	printf("%d", ans/2);
}