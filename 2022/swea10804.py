T = int(input())
ans=""
for case in range(1, T + 1):
    get = input()
    p=""
    for i in get:
        if i =='p':
            p='q'+p
        elif i =='q':
            p='p'+p
        elif i == 'b':
            p='d'+p
        elif i =='d':
            p='b'+p
    ans += f"#{case} {p}\n"
print(ans)