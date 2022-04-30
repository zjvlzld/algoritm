n=int(input())

ans=1
add=0
while(True):
    add+=ans
    if(add>n):
        print(ans-1)
        break
    ans+=1