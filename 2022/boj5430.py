from collections import deque
T=int(input())

for _ in range(T):
    get=input()
    n=int(input())
    d=deque()
    nums=input()
    if(n!=0):
        nums=list(map(int,nums[1:-1].split(',')))
        for i in nums:
            d.append(i)
    direction=True
    c=True
    for i in get:
        if i=='R':
            direction= not direction
        else:
            if(len(d)==0):
                print('error')
                c=False
                break
            if direction:
                d.popleft()
            else:
                d.pop()
    if(len(d)>0):
        if(direction):
            print('[',end="")
            for i in range(len(d)-1):
                print(f"{d[i]},",end="")
            print(f"{d[-1]}]")            
        else:
            print('[',end="")
            for i in range(len(d)-1,0,-1):
                print(f"{d[i]},",end="")
            print(f"{d[0]}]")     
    if(len(d)==0 and c):
        print([])