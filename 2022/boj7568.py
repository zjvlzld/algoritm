n=int(input())

people=[[0,0] for _ in range(n)]
ans=[0 for _ in range(n+1)]
for i in range(n):
    people[i]=[int(x) for x in input().split(" ")]

for i in range(n):
    ans=0
    for j in range(n):
        if(people[i][0]<people[j][0] and people[i][1]<people[j][1]):
            ans+=1
    print(ans+1)
