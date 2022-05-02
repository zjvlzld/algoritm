count=int(input())

cal=[x for x in input().split(" ")]

mini=''
maxi=''

def solution(now,less):
    global mini
    global maxi
    if(len(now)==count+1):
        if(len(mini)==0):
            for i in now:
                mini+=str(i)
        maxi=''
        for i in now:
            maxi+=str(i)
        return
    if len(now)==0:
        for i in less:
            now.append(i)
            less.remove(i)
            solution(now,less)
            now.pop()
            less.append(i)
            less.sort()
        return
    else:
        for i in less:
            if(cal[len(now)-1]=='>'):
                if(now[-1]>i):
                    now.append(i)
                    less.remove(i)
                    solution(now,less)
                    now.remove(i)
                    less.append(i)
                    less.sort()
            else:
                if(now[-1]<i):
                    now.append(i)
                    less.remove(i)
                    solution(now,less)
                    now.remove(i)
                    less.append(i)
                    less.sort()

solution([],[0,1,2,3,4,5,6,7,8,9])

print(maxi)
print(mini)

