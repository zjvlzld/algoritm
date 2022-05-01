import sys
sosu=[1]*1000001
sosu[0]=0
sosu[1]=0
for i in range(2,1000001):
    if(sosu[i]==1):
        for j in range(2,1000001):
            if(i*j>1000000):
                break
            sosu[i*j]=0

while True:
    get=int(sys.stdin.readline())
    if(get==0):
        break
    check=0
    for i in range(3,get+1):
        if(sosu[i]==1 and sosu[get-i]==1):
            print(get,'=',i,'+',get-i)
            check=1
            break
    if(check==0):
        print("Goldbach's conjecture is wrong.")