a=input()
cal=input()
b=input()

if(cal=='*'):
    print('1',end="")
    for _ in range(len(a)+len(b)-2):
        print('0',end="")
if(cal=='+'):
    if(len(a)<len(b)):
        print('1',end="")
        for _ in range(len(b)-len(a)-1):
            print('0',end="")
        print(a)
    elif (len(a)>len(b)):
        print('1',end="")
        for _ in range(len(a)-len(b)-1):
            print('0',end="")
        print(b)
    else:
        print('2',end="")
        for _ in range(len(a-1)):
            print("0",end="")
