import sys
t=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split()]

sosu=[1]*1001
sosu[0]=0
sosu[1]=0
for i in range(2,1001):
    if(sosu[i]==1):
        for j in range(2,1001):
            if(i*j>1000):
                break
            sosu[i*j]=0
ans=0
for i in range(t):
    ans+=sosu[nums[i]]
print(ans)