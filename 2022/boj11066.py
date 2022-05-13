t=int(input())

for _ in range(t):
    k=int(input())
    nums=[0]+list(map(int,input().split()))
    dp=[[0]*(k+1) for _ in range(k+1)]
    # dp[i][j]는 i~j까지 최소의 합
    for i in range(2, k+1): # i값은 길이를 의미이므로 2부터 시작
        for j in range(1, k+1-(i-1)): #
            dp[j][j+i-1] = min(dp[j][j+n]+dp[j+n+1][j+i-1] for n in range(i-1) )+sum(nums[j:j+i])    
    print(dp[1][k])