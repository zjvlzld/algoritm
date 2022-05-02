a,b=map(int, input().split(" "))

get=[x for x in input().split(" ")]
moum=['a','e','i','o','u']
get.sort()
def solution(c1,c2,now,s):
    if(c1+c2==a):
        if(c1<1 or c2<2):
            return
        else:
            for i in now:
                print(i,end="")
            print()
            return
    else:
        for i in range(s,b):
            if not (get[i] in now):
                now.append(get[i])
                if (get[i] in moum):
                    solution(c1+1,c2,now,i+1)
                else:
                    solution(c1,c2+1,now,i+1)
                now.pop()
    return
solution(0,0,[],0)