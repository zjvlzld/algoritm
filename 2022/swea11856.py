from math import fabs


T = int(input())

ans=""
for case in range(1,T+1):
    al=dict()

    get=input()

    for i in range(len(get)):
        if al.get(get[i])==None:
            al.update({get[i]:1})
        else:
            al[get[i]]+=1
    if(len(al)!=2):
        ans+="#"+str(case)+"No\n"
    else:
        v=al.values()
        check=True
        for i in v:
            if(i!=2):
                ans+="#"+str(case)+"No\n"
                check=False
                break
        if(check):
                ans+="#"+str(case)+"Yes\n"
    print(al)
print(ans)
