get=input()
while get!='0':
    ans=len(get)+1
    for i in get:
        if(i=='1'):
            ans+=2
        elif(i=='0'):
            ans+=4
        else:
            ans+=3
    print(ans)
    get=input()