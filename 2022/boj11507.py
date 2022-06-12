get=input()
p=[0 for _ in range(13)]
k=[0 for _ in range(13)]
h=[0 for _ in range(13)]
t=[0 for _ in range(13)]
for i in range(0,len(get),3):
    n=int(get[i+1])*10+int(get[i+2])
    if get[i]=="P":
        if(p[n]==0):
            p[n]=1
        else:
            print("GRESKA")
            exit()
    if get[i]=="K":
        if(k[n]==0):
            k[n]=1
        else:
            print("GRESKA")
            exit()
    if get[i]=="T":
        if(t[n]==0):
            t[n]=1
        else:
            print("GRESKA")
            exit()
    if get[i]=="H":
        if(h[n]==0):
            h[n]=1
        else:
            print("GRESKA")
            exit()
print(f"{13-sum(p)} {13-sum(k)} {13-sum(h)} {13-sum(t)}")