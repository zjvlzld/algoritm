import sys
a,b=[int(x) for x in sys.stdin.readline().split()]

sosu=[1]*1000001
sosu[0]=0
sosu[1]=0
for i in range(2,1000001):
    if(sosu[i]==1):
        for j in range(2,1000001):
            if(i*j>1000000):
                break
            sosu[i*j]=0
for i in range(a,b+1):
    if(sosu[i]==1):
        print(i)