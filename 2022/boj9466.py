import sys
T = int(sys.stdin.readline())
sys.setrecursionlimit(2000000)
for _ in range(T):
    n = int(sys.stdin.readline())
    check = [0 for _ in range(n+1)]
    go = [int(x) for x in sys.stdin.readline().rstrip().split()]
    go = [0]+go
    visit = [0 for _ in range(n + 1)]
    for i in range(1, n+1):
        if check[i] == 0:
            def solution(now):
                p = now[-1]
                if check[go[p]] != 0:
                    for k in now:
                        check[k] = -1
                    return
                if visit[go[p]] == 1:
                    checker = False
                    for k in now:
                        if k == go[p]:
                            checker = True
                        if checker:
                            check[k] = 1
                        else:
                            check[k] = -1
                    return
                visit[go[p]] = 1
                now.append(go[p])
                solution(now)
            visit[i] = 1
            solution([i])

    ans = 0
    for i in check:
        if i == -1:
            ans += 1
    print(ans)
