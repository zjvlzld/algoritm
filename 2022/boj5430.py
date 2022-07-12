from collections import deque
T=int(input())

for _ in range(T):
    get=input()
    n=int(input())
    d=deque()
    nums=input()#인풋 받은 값인데 [1,2,...n] 형식이다
    if(n!=0):#길이가 0보다 크면 d라는 deque에 값을 넣어준다
        nums=list(map(int,nums[1:-1].split(',')))
        for i in nums:
            d.append(i)
    direction=True #뒤집혀있는지 아닌지 확인하는 변수
    c=True#에러를 출력 했는지 아닌지 확인하는 변수
    for i in get:
        if i=='R':#R이면 방향을 바꿔 뒤집힌 배열로 인식
            direction= not direction
        else:
            if(len(d)==0):#길이가 0인데 값을 빼려 할 경우
                print('error')#에러출력 후
                c=False#에러났었던 것을 변수에 저장
                break
            if direction:#정방향이면
                d.popleft()#앞에서
            else:#아니면
                d.pop()#뒤에서
    if(len(d)>0):#결과 배열의 길이가 0보다 크면
        if(direction): #정방향이면 앞에서 부터 출력
            print('[',end="")
            for i in range(len(d)-1):
                print(f"{d[i]},",end="")
            print(f"{d[-1]}]")            
        else:#아니면 뒤에서부터
            print('[',end="")
            for i in range(len(d)-1,0,-1):
                print(f"{d[i]},",end="")
            print(f"{d[0]}]")     
    if(len(d)==0 and c):#만약 결과 배열의 길이가 0인데 오류 출력을 안했으면
        print('[]')#[]를 출력해주자