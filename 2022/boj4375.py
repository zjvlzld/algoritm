while(True):
    n='1'
    try:
        get=int(input())

        while True:
            if(int(n)%get==0):
                print(len(n))
                break
            n+='1'
    except:
        break