import sys

n = int(sys.stdin.readline())
check = [0 for _ in range(n+1)]
sosu = []

for i in range(2, n+1):
    if check[i] == 0:
        check[i] = 1
        sosu.append(i)
        for j in range(i, n+1, i):
            check[j] = 1
s = 0
e = 0
if n == 1:
    print(0)
    exit()
now = sosu[0]
ans = 0
while s < len(sosu):
    if now == n:
        ans += 1
        if e < len(sosu)-1:
            e += 1
            now += sosu[e]
        else:
            now -= sosu[s]
            s += 1
    elif now < n:
        if e < len(sosu)-1:
            e += 1
            now += sosu[e]
        else:
            print(ans)
            exit()
    elif now > n:
        now -= sosu[s]
        s += 1

print(ans)