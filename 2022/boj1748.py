import sys
get=int(sys.stdin.readline())

digit=1
mul=1
ans=0
while get>digit*9:
    ans+=mul*digit*9
    mul+=1
    get-=digit*9
    digit*=10

ans+=get*mul
print(ans)

