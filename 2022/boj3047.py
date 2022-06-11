nums=[int(x) for x in input().split(' ')]
get=input()
nums.sort()
for i in get:
    print(nums[ord(i)-ord('A')],end=" ")
print()