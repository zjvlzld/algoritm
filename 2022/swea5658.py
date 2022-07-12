T=int(input())
digit=['0','1','2','3','4','5','6','7','8','9']
for test in range(1,T+1):
    N,K=map(int,input().split(' '))
    get=input()
    nums=[]
    for i in range(N):
        t=0# 해당 위치에서 만들 수 있는 수를 넣을 변수
        for j in range(N//4):
            if(get[(i+j)%N] in digit):
                t+=int(get[(i+j)%N])*16**((N//4)-1-j)
            else:
                t+=(ord(get[(i+j)%N])-ord('A')+10)*16**((N//4)-1-j)
        if t not in nums:# 중복체크
            nums.append(t)
    nums.sort(reverse=True)
    print(f"#{test} {nums[K-1]}")