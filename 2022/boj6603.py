while True:
    get=[int(i) for i in input().split(" ")]
    if get[0]==0:
        break
    def solution(now):
        if(len(now)==0):
            for i in range(1,len(get)):
                now.append(get[i])
                solution(now)
                now.pop()
            return
        if(len(now)==6):
            for i in now:
                print(i,end=" ")
            print()
            return
        for i in range(1,len(get)):
            if(get[i]>now[-1]):
                now.append(get[i])
                solution(now)
                now.pop()
        return
    solution([]) 
    print()       

