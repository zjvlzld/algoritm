import sys

n=int(sys.stdin.readline())

nums=[0 for _ in range(26)]
for _ in range(n):
    get=sys.stdin.readline().rstrip()

    for i in range(len(get)):
        nums[ord(get[i])-ord('A')]+=10**(len(get)-1-i)
nums.sort(reverse=True)
ans=0
for i in range(9):
    ans+=(9-i)*nums[i]

print(ans)