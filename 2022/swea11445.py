T = int(input())

for case in range(1,T+1):
    a=input().replace(" ",'')
    b=input().replace(" ",'')
    if(b==a+'a'):
        print(f"#{case} Y")
    else:
        print(f"#{case} N")