get=input()
while(get!='0'):
    check=True
    for i in range(len(get)//2):
        if(get[i]!=get[len(get)-i-1]):
            check=False
            break
    if(check):
        print('yes')
    else:
        print('no')
    get=input()