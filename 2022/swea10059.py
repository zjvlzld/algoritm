T = int(input())

for case in range(1,T+1):
    num=int(input())
    if(0<num//100<13):
        if(0<num%100<13):
            print(f'#{case} AMBIGUOUS')
        else:
            print(f'#{case} MMYY')
    else:
        if(0<num%100<13):
            print(f'#{case} YYMM')
        else:
            print(f'#{case} NA')
