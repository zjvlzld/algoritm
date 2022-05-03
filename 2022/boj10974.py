from importlib.abc import SourceLoader


t=int(input())

def solution(now):
    if len(now)==t:
        for i in now:
            print(i,end=" ")
        print()
        return
    for i in range(1,t+1):
        if not (i in now):
            now.append(i)
            solution(now)
            now.pop()

solution([])