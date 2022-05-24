T = int(input())

for case in range(1, T+1):
    a,b=map(int, input().split())

    p = "ON"
    for i in range(a):
        if(b==0):
            p="OFF"
            break
        if(b%2==0):
            p = "OFF"
            break
        b //=2
    print(f"#{case} {p}\n")