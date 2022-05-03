t=int(input())

cost=[]
for _ in range(t):
    cost.append([int(x) for x in input().split(" ")])

visit=[0 for _ in range(t)]
ans=10000001
def solution(nowPosition,nowCost,count):
    global ans
    if(count==t-1):
        for i in range(t):
            if visit[i]==2:
                s=i
        if(cost[nowPosition][s]!=0):
            ans=min(ans,nowCost+cost[nowPosition][s])
        return
    if(nowPosition==-1):
        for n in range(t):
            visit[n]=2
            for d in range(t):
                if(visit[d]==0 and cost[n][d]!=0):
                    solution(d,nowCost+cost[n][d],count+1) 
            visit[n]=0
    else:
        visit[nowPosition]=1
        for d in range(t):
            if(visit[d]==0 and cost[nowPosition][d]!=0):
                solution(d,nowCost+cost[nowPosition][d],count+1) 
        visit[nowPosition]=0     
solution(-1,0,0)
print(ans)

            
