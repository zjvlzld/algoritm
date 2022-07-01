

a,b,c=map(int,input().split(' '))
a%=c

def solution(n):
    if(n==1):
        return a
    r=solution(n//2)
    if(n%2==0):
        return (r*r)%c
    else:
        return (r*r*a)%c

print(solution(b))