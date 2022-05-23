T = int(input())

for case in range(1, T+1):
    goal = int(input())
    days = [int(x) for x in input().split()]
    dp=[[0,0,0,0,0,0,0]for _ in range(7)]
    for i in range(7):
        dp[i][6]=sum(days)
        for j in range(6):
            for k in range(j+1):
                dp[i][j] += days[(i+k)%7]
    ans=goal//sum(days)*7
    goal %= sum(days)
    if(goal==0):
        ans -= 7
        goal=sum(days)
    add=7
    for i in range(7):
        for j in range(7):
            if(goal==dp[i][j]):
                if(add>j):
                    add=j+1
    print(f"#{case} {ans+add}")