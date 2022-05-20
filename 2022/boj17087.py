import sys
N, S = map(int, sys.stdin.readline().split(' '))
nums = [int(x) for x in sys.stdin.readline().split(' ')]

ans = 0


def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(a % b, b)


for i in range(N):
    nums[i] = abs(S-nums[i])
now=nums[0]
for i in range(1,N):
    now=gcd(now,nums[i])

print(now)