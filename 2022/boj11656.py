ans=[]
get=input()
for i in range(len(get)):
    ans.append(get[i:])
ans.sort()
for i in ans:
    print(i)