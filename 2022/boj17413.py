get=input()
check=True
t=''
for i in get:
    if(check):
        if(i=='<'):
            for j in range(len(t)-1,-1,-1):
                print(t[j],end="")
            t=''
            print(i,end="")
            check=False     
            
        elif i==' ':
            for j in range(len(t)-1,-1,-1):
                print(t[j],end="")
            print(' ',end="")
            t=''
        else:
            t+=i
    elif i=='>':
        print(i,end="")
        check=True     
    else:
        print(i,end="")
for j in range(len(t)-1,-1,-1):
    print(t[j],end="")
print()