#define _CRT_SECURE_NO_WARNINGS

#include<cstdio>

using namespace std;

char c[9];
bool used[10];
int main()
{
	int n;
	char get;
	scanf("%d", &n);
	scanf("%c", &get);
	for (int i = 0;i < n; i++)
	{
		scanf("%c", &c[i]);
		scanf("%c", &get);
	}

	for (int i = 0; i<n; i++)
	{
		int p = 0;
		int now = i;
		while (c[now] == '<')
		{
			p++;
			now++;
		}
		int point = 0;
		for (int i = 9; i >= 9 - n; i--)
		{
			if (used[i] == false)
			{
				if (point == p)
				{
					printf("%d", i);
					used[i] = true;
				}
				point++;
			}
		}
	}
	for (int i = 9; i >= 0; i--)
	{
		if (used[i] == false)
		{
			printf("%d\n", i);
			break;
		}
	}


	for (int i = 0; i < n + 1; i++)
	{
		used[i] = false;
	}

	for (int i = 0; i < n; i++)
	{
		int p = 0;
		int now = i;
		while (c[now] == '>')
		{
			p++;
			now++;
		}
		int point = 0;
		for (int i = 0; i < n+1; i++)
		{
			if (used[i] == false)
			{
				if (point == p)
				{
					printf("%d", i);
					used[i] = true;
				}
				point++;
			}
		}
	}
	for (int i = 0; i < n + 1; i++)
	{
		if (used[i] == false)
		{
			printf("%d\n", i);
			break;
		}
	}


}