T = int(input())

for case in range(1,T+1):
    n=int(input())
    dosi=[[]]
    for _ in range(n):
        dosi.append([int(x) for x in input().split()])
    threat=[[]for _ in range(n+1)]
    for i in range(1,n):
        for j in range(i+1,n+1):
            dist=(dosi[i][0]-dosi[j][0])**2+(dosi[i][1]-dosi[j][1])**2
            if(dosi[i][2]/dist>dosi[j][2]):
                threat[j].append(i)
            if(dosi[j][2]/dist>dosi[i][2]):
                threat[i].append(j)
    
    print("#"+str(case)+" ",end="")

    for i in range(1,n+1):
        if(len(threat[i])==0):
            print('K',end=" ")
        elif(len(threat[i])>1):
            print("D",end=" ")

        else:
            now=i
            while(len(threat[now])==1):
                now=threat[now][0]

            if(len(threat[now])==0):
                print(now,end=" ")
            else:
                print('D',end=" ")

    print()
