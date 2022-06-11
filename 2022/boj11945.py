a,b=map(int,input().split(' '))

for _ in range(a):
    get=input()
    for i in range(b):
        print(get[b-1-i],end="")
    print()