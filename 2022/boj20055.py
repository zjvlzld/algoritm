from logging import RootLogger
import sys


n,e=map(int,sys.stdin.readline().split(" "))

belt=[int(x) for x in sys.stdin.readline().split(" ")]
robots=[0 for _ in range(2*n)]
s=0
end=n-1
ans=0
while True:
    ans+=1
    #컨베이어벨트 이동
    end=(end-1)%(2*n)
    s=(s-1)%(2*n)
    #로봇이 엔드 위치에 있으면 방출
    robots[end]=0

    #로봇 전진
    #맨뒤 바로 앞 칸에서 부터
    for i in range(n-1):
        if robots[ (end-1-i)%(2*n) ]==1:

            if belt[(end-i)%(2*n)]>0 and robots[(end-i)%(2*n)]==0:
                belt[(end-i)%(2*n)]-=1
                robots[(end-i)%(2*n)]=1
                robots[(end-1-i)%(2*n)]=0

    #이동했는데 로봇이 마지막에 있으면 방출
    robots[end]=0
    #belt의 내구도 체크
    if(belt[s]>0):
        robots[s]=1
        belt[s]-=1
    count=0
    for i in belt:
        if i <1:
            count+=1
        if count>=e:
            print(ans)
            exit()
