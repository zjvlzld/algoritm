import copy
n=int(input())
c=[0 for _ in range(n*50+1)]
def solution(d,now):
    if(len(d)==4):
        temp=1*d[0]+5*d[1]+10*d[2]+d[3]*50
        c[temp]=1
        return
    if(len(d)==3):
        t=copy.deepcopy(d)
        t.append(now)
        solution(t,0)
    else:
        for i in range(now+1):
            t=copy.deepcopy(d)
            t.append(i)
            solution(t,now-i)
solution([],n)
print(sum(c))