import sys
T=int(input())
S=[-1 for _ in range(21)]
for _ in range(T):
    get=sys.stdin.readline().rstrip().split(" ")
    if(get[0]=='add'):
        S[int(get[1])]=1
        continue
    elif(get[0]=='remove'):
        S[int(get[1])]=-1
        continue
    elif(get[0]=='check'):
        if S[int(get[1])]==1:
            print(1)
        else:
            print(0)
        continue
    elif(get[0]=='toggle'):
        S[int(get[1])]*=-1
        continue
    elif(get[0]=='all'):
        S=[1 for _ in range(21)]
        continue
    elif(get[0]=='empty'):
        S=[-1 for _ in range(21)]
        continue