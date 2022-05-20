T = int(input())
for t in range(1, T+1):
    ans = 0

    n, r = map(int, input().split(" "))
    nums = [int(x) for x in input().split(' ')]
    dp = [[0,0] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i][0] += 1
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                dp[i][1] += 1
    print((((1+(r-1))*(r-1)) //2)) 
    for i in range(n):
        ans+=(dp[i][0]+dp[i][1])*(((1+(r-1))*(r-1))//2)+(dp[i][1])*r
        ans %=1000000007
    print('#'+str(t), ans)
