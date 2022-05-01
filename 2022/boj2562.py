get=[]
for i in range(9):
    get.append([i+1,int(input())])
get.sort(key=lambda x : -x[1])
print(get[0][1])
print(get[0][0])