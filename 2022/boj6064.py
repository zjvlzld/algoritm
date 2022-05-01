T=int(input())
for _ in range(T):
    x,y,a,b=map(int,input().split(" "))
    check=-1
    if(x>y):
        for i in range(x+1):
            if((x*i+a)%y==b):
                print(x*i+a)
                check=1
                break
            if((x*i+a)%y==0 and y==b):
                print(x*i+a)
                check=1
                break
        if(check==-1):
            print(check)
    else:
        for i in range(y+1):
            if((y*i+b)%x==a):
                print(y*i+b)
                check=1
                break
            if((y*i+b)%x==0 and a==x):
                print(y*i+b)
                check=1
                break
        if(check==-1):
            print(check)
