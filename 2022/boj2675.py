T=int(input())
for _ in range(T):
    a,b=input().split(" ")
    a=int(a)
    for i in range(len(b)):
        for _ in range(a):
            print(b[i],end="")

    print()