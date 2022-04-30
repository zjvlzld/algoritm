T=int(input())
ans=[0 for _ in range(T)]
for i in range(T):
    gets=[int(x) for x in input().split()]

    gets.sort()
    if(gets[0]==gets[1] and gets[1]==gets[2]):
        ans[i]=10000+gets[0]*1000
    elif(gets[0]==gets[1]):
        ans[i]=(1000+100*gets[0])
    elif(gets[1]==gets[2]):
        ans[i]=(1000+100*gets[1])
    else:
        ans[i]=(100*gets[2])

print(max(ans))