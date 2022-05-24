T = int(input())
ans = ""
for case in range(1, T + 1):
    dp = [0 for _ in range(26)]
    get = input()

    for i in get:
        dp[ord(i) - ord('a')] += 1
    t = ""
    for i in range(26):
        if dp[i] % 2 == 1:
            t += chr(ord('a')+i)
    if len(t) == 0:
        ans = ans + "#" + str(case) + " Good\n"
    else:
        ans = ans + "#" + str(case) + " " + t + "\n"

print(ans)