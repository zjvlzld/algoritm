T = int(input())

for t in range(1, T + 1):
    get = input()
    if get == 'MON':
        print(f"#{t} 6")
    if get == 'THU':
        print(f"#{t} 5")
    if get == 'WED':
        print(f"#{t} 4")
    if get == 'THU':
        print(f"#{t} 3")
    if get == 'FRI':
        print(f"#{t} 2")
    if get == 'SAT':    
        print(f"#{t} 1")
    if get == 'SUN':
        print(f"#{t} 7")
