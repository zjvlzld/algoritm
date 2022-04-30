from cmath import pi
import math
T=int(input())

for t in range(T):
    gets=input().split(" ")
    gets[0]=float(gets[0])
    for i in range(1,len(gets)):
        if(gets[i]=='@'):
            gets[0]=gets[0]*3
        if(gets[i]=='%'):
            gets[0]=gets[0]+5
        if(gets[i]=='#'):
            gets[0]=gets[0]-7
    print( "{:.2f}".format(gets[0]))

print('10칸 0채움 소수점 1자리 출력 :%8.4f'%12.123)