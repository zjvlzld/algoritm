import sys
import copy
n=int(sys.stdin.readline())

ans=0
put=[]
def solution(i):
    global ans
    global put
    check=[]
    for j in range(len(put)):
        check.append(put[j])
        check.append(put[j]+(i-j))
        check.append(put[j]-(i-j))
    for j in range(n):
        if(i==n-1):
            if(j in check):
                continue
            else:
                ans+=1
                return
        if j in check:
            continue
        else:
            put.append(j)
            solution(i+1)
            put.pop()
solution(0)
print(ans)