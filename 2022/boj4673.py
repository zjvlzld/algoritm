check=[0 for _ in range(10001)]
ans=[]
for i in range(1,10001):
    if(check[i]==0):
        ans.append(i)
        t=i
        while(t<10001):
            check[t]=1
            t1=str(t)
            for j in t1:
                t+=int(j)
    else:
        continue
for i in ans:
    print(i)