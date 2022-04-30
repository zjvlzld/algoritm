#include<iostream>
#include<string>

using namespace std;

bool check[21];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int c;
	cin>>c;
	for (int i = 0; i < c; i++)
	{
		string st;
		cin >> st;
		if (st == "add")
		{
			int get;
			cin >> get;
			check[get] = true;

		}
		if (st == "remove")
		{
			int get;
			cin >> get;
			check[get] = false;

		}
		if (st == "check")
		{
			int get;
			cin >> get;
			if (check[get])
			{
				cout << "1\n";
			}
			else
			{
				cout << "0\n";
			}
			
		}
		if (st == "toggle")
		{
			int get;
			cin >> get;
			check[get] = !check[get];
		}
		if (st == "all")
		{
			for (int i = 0; i < 21; i++)
			{
				check[i] = true;
			}
		}
		if (st == "empty")
		{
			for (int i = 0; i < 21; i++)
			{
				check[i] = false;
			}
		}
	}
}