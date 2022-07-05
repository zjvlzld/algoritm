a,b,c=map(int,input().split(' '))
a%=c #미리 나머지를 구해둔다

def solution(n):
    if(n==1):
        return a

    r=solution(n//2)#(a^(n//2))%c를 구한다 
    
    if(n%2==0):#2로 나누어 떨어지면
        return (r*r)%c #((a^(n//2))%c * (a^(n//2))%c)%c는 (a^(n))%c를 활용해서 리턴하고
    else:#홀수이면
        return (r*r*a)%c # 추가로 a를 곱한 후 나머지를 구해서 리턴한다

print(solution(b))