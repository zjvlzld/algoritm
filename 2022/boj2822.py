sc=[]
s=0
for i in range(1,9):
    b=int(input())
    sc.append([i,b])
sc.sort(key=lambda x:x[1],reverse=True)

ans=sc[:5]

ans.sort(key=lambda x:x[0])
s=0
p=""
for i in ans:
    s+=i[1]
    p=p+str(i[0])+' '
print(s)
print(p)