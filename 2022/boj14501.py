end=int(input())
chart=[]
chart.append([0,0])
for _ in range(end):
    chart.append([int(x) for x in input().split(" ")])
ans=0
def solution(day,cost):
    global ans
    if(day>end):
        ans=max(ans,cost)
        return
    if(day+chart[day][0]<=end+1):
        solution(day+chart[day][0],cost+chart[day][1])
    solution(day+1,cost)        
solution(1,0)
print(ans)
