import sys

N = int(sys.stdin.readline())

ans = 1
for i in range(2, N+1):
    ans *= i
    while ans % 10 == 0:
        ans //= 10
    ans %= 1000000000

print(ans % 10)
