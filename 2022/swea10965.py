

sosu=[2]
for i in range(3,int((10**7)**(1/2)),2):
    for j in sosu:
        if i%j==0:
            break
    else:
        sosu.append(i)
T = int(input())
p=""            
for case in range(1, T+1):
    get = int(input())
    if get == 1:
        p+="#"+str(case)+' 1\n'
        continue
    ans = 1
    if(get**(1/2)==int(get**1/2)):
        p+="#"+str(case)+' 1\n'
        continue
    for d in sosu:
        count=0
        while get%d == 0:
            get//=d
            count+=1
        if count%2 ==1 :
            ans*=d
        if(get==1):
            break
    p+="#"+str(case)+" "+str(ans)+'\n'

print(p)