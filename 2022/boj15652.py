import sys

a,b=map(int,sys.stdin.readline().split())

def solution(now,num,length,s):
    if(len(now)==length):
        for i in now:
            print(i,end=" ")
        print()
        return
    for i in range(s,num+1):
        now.append(i)
        solution(now,num,length,i)
        now.remove(i)

solution([],a,b,1)