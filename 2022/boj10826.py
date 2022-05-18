import sys

nums = [0 for _ in range(10001)]
nums[1] = 1

n = int(sys.stdin.readline())

for i in range(2, n+1):
    nums[i] = nums[i-1] + nums[i-2]

print(nums[n])
