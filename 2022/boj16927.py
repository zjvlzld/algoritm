import sys
n,m,r=map(int,sys.stdin.readline().split(" "))

nums=[]

for _ in range(n):
    nums.append([int(x) for x in sys.stdin.readline().split(" ")])


def solution(d):
    Count=(n-2*d)*2+2*(m-2*d-2)
    Count=r%Count
    q=[]
    for i in range(m-2*d-1):
        q.append(nums[d][d+i])
    for i in range(n-2*d-1):
        q.append(nums[d+i][m-d-1]) 
    for i in range(m-2*d-1):       
        q.append(nums[n-d-1][m-d-1-i])
    for i in range(n-2*d-1):
        q.append(nums[n-d-1-i][d])
    q=q[Count:]+q[:Count]
    for i in range(m-2*d-1):
        nums[d][d+i]=q[0]
        q.pop(0)
    for i in range(n-2*d-1):
        nums[d+i][m-d-1]=q[0]
        q.pop(0) 
    for i in range(m-2*d-1):       
        nums[n-d-1][m-d-1-i]=q[0]
        q.pop(0)
    for i in range(n-2*d-1):
        nums[n-d-1-i][d]=q[0]
        q.pop(0)

for i in range(min(n,m)//2):
    solution(i)

for z in nums:
    for i in z:
        print(i,end=" ")
    print()