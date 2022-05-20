import sys
sys.setrecursionlimit(1000000000)

T = int(sys.stdin.readline())


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(a % b, b)


for _ in range(T):
    nums = [int(x) for x in sys.stdin.readline().split(" ")]
    ans = 0
    for i in range(1, nums[0]):
        for j in range(i+1, nums[0]+1):
            ans += gcd(nums[i], nums[j])
    print(ans)
