get=input()
p=''
ans=''
for i in range(len(get)):
    if(get[i]==':'):
        if(get[i-1]==':'):
            if(i==len(get)-1):
                ans+='p'
            else:
                ans+='p:'
        elif(i!=0):    
            while len(p)!=4:
                p='0'+p
            ans+=p+":"
        p=''
    else:
        p=p+str(get[i])
if(len(p)!=0):
    while len(p)!=4:
        p='0'+p
    ans+=p
print(ans)
for i in range(len(ans)):
    if(ans[i] =='p'):
        if(i==len(ans)-1):
            for _ in range((39-len(ans))//5):
                print('0000:',end="")
            print("0000")
        else:
            for _ in range((39-len(ans))//5):
                print('0000:',end="")
            print("0000",end="") 
    else:
        print(ans[i],end="")