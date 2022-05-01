T=int(input())

for _ in range(T):
    a=b=0
    for _ in range(9):
        g1,g2=map(int,input().split())
        a+=g1
        b+=g2
    if(a>b):
        print('Yonsei')
    elif(a<b):
        print("Korea")
    else:
        print('Draw')
    