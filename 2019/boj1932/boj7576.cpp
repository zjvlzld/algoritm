#include <stdio.h>
#include <queue>

using namespace std;
int tomato[1000][1000];
int x,y;
int ans;
queue<pair<int , int>> stp;

int main()
{
    scanf("%d %d",&x,&y);
    for(int i=0;i<y;i++)
    {
        for(int j=0;j<x;j++)
        {
            scanf("%d",&tomato[j][i]);
            if(tomato[j][i]==1)
            {
                pair<int, int> t;
                t=make_pair(j,i);
                stp.push(t);
            }
        }
    }

    while(!stp.empty())
    {
        pair<int,int> now=stp.front();
        stp.pop();
        if(now.first>0&&tomato[now.first-1][now.second]==0)
        {
            tomato[now.first-1][now.second]=tomato[now.first][now.second]+1;
            pair<int,int> temp=make_pair(now.first-1,now.second);
            stp.push(temp);
        }
        if(now.first<x-1&&tomato[now.first+1][now.second]==0)
        {
            tomato[now.first+1][now.second]=tomato[now.first][now.second]+1;
            pair<int,int> temp=make_pair(now.first+1,now.second);
            stp.push(temp);
        }
        if(now.second>0&&tomato[now.first][now.second-1]==0)
        {
            tomato[now.first][now.second-1]=tomato[now.first][now.second]+1;
            pair<int,int> temp=make_pair(now.first,now.second-1);
            stp.push(temp);
        }
        if(now.second<y-1&&tomato[now.first][now.second+1]==0)
        {
            tomato[now.first][now.second+1]=tomato[now.first][now.second]+1;
            pair<int,int> temp=make_pair(now.first,now.second+1);
            stp.push(temp);
        }
    }
    for(int i=0;i<y;i++)
    {
        for(int j=0; j<x;j++)
        {
            if(tomato[j][i]==0)
            {
                printf("-1");
                return 0;
            }
            if(ans<tomato[j][i])
            {
                ans=tomato[j][i];
            }
        }
    }
    printf("%d",ans-1);
}