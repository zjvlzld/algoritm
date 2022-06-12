a,b=map(int,input().split(' '))

nums=list(int(x) for x in input().split(" "))

for i in nums:
    print(i-a*b,end=" ")
print()