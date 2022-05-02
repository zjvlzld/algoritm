get=int(input())

score=[]
for _ in range(get):
    score.append([int(x) for x in input().split()])
ans=40000
check=[False for _ in range(get)]

def solution(count,now):
    global ans
    if(count==get//2):
        teama=0
        teamb=0
        for i in range(get-1):
            for j in range(i,get):
                if(check[i]==check[j]==True):
                    teama+=score[i][j]+score[j][i]
                if(check[i]==check[j]==False):
                    teamb+=score[i][j]+score[j][i]
        ans=min(abs(teama-teamb),ans)
        return
    for i in range(now,get):
        check[i]=True
        solution(count+1,i+1)
        check[i]=False

solution(0,0)
print(ans)
