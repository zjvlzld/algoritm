n=input()

ans=0
for i in range(1,int(n)+1):
    if(len(str(i))<3):
        ans+=1
        continue
    else:
        g=int(str(i)[0])-int(str(i)[1])
        for j in range(1,len(str(i))-1):
            if(int(str(i)[j])-g != int(str(i)[j+1])):
                ans-=1
                break
        ans+=1

print(ans)