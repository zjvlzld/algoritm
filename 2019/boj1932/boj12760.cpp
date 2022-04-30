#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int cards[101][101];
int score[101];
int main()
{
    int people,card;
    scanf("%d %d",&people, &card);
    for(int i=1;i<people+1;i++)
    {
        for(int j=0;j<card;j++)
        {
            scanf("%d",&cards[i][j]);
        }
    }
    for(int i=1;i<people+1;i++)
    {
        sort(cards[i],cards[i]+card);
    }
    for(int j=0;j<card;j++)
    {
        int top=0;
        vector<int> winnerwinnerchickendinner;
        for(int i=1;i<people+1;i++)
        {
            if(top==cards[i][j])
            {
                winnerwinnerchickendinner.push_back(i);
            }

            if(top<cards[i][j])
            {
                winnerwinnerchickendinner.clear();
                top=cards[i][j];
                winnerwinnerchickendinner.push_back(i);
            }
        }
        for(int i=0;i<winnerwinnerchickendinner.size();i++)
        {
            score[winnerwinnerchickendinner[i]]++;
        }   
    }
    int top=0;
    for(int i=1;i<people+1;i++)
    {
        if(top<score[i])
        {
            top=score[i];
        }
    }
    for(int i=1;i<people+1;i++)
    {
        if(top==score[i])
        {
            printf("%d ",i);
        }
    }
    return 0;
}