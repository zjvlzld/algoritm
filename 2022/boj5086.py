from posixpath import split


while True:
    a,b=map(int,input().split(" "))
    if(a==b==0):
        break
    if(a%b==0 or b%a==0):
        if(a//b>=1):
            print('multiple')
        else:
            print('factor')
    else:
        print('neither')
