get=input()
o=['a','e','i','o','u','A','E','I','O','U']
while get!='#':
    ans=0
    for i in get:
        if i in o:
            ans+=1
    print(ans)
    get=input()