T = int(input())

ans=""
nums=set()
for i in range(1,10):
    for j in range(1,10):
        nums.add(i*j)
for case in range(1,T+1):
    get=int(input())
    if(get in nums):
        ans+="#"+str(case)+" Yes\n"
    else:
        ans+="#"+str(case)+" No\n"

print(ans)