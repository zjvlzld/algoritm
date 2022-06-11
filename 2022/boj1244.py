n=int(input())
switch=[int(x) for x in input().split(' ')]
s=int(input())
for _ in range(s):
    a,b=map(int,input().split(' '))
    if a==1:
        for i in range(b-1,n,b):
            switch[i]=abs(switch[i]-1)
    if(a==2):
        for i in range(n):
            if(b-1+i>=n or b-1-i<0 or switch[b-1-i]!=switch[b-1+i]):
                break
            switch[b-1+i]=abs(switch[b-1+i]-1)
            switch[b-i-1]=switch[b+i-1]
i=0
for _ in range(n):
    print(switch[i],end=' ')
    if(i%20==19):
        print()

    i+=1 