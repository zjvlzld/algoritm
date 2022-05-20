import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split(' '))
    ans = a//(2*b+1)
    if a % (2*b+1) != 0:
        ans += 1
    print(ans)