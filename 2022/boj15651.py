import sys

def solution(now,end,num):
    if(len(now)==end):
        for i in range(end):
            print(now[i], end=" ")
        print()
        return

    for i in range(1,num+1):
        now.append(i)
        solution(now,end,num)
        now.pop()

a,b=map(int,input().split(" "))
solution([],b,a)


        
