
get=input()
get=get.upper()
count=[]
for i in range(26):
    count.append([0,chr(65+i)])
for i in get:
    count[ord(i)-ord('A')][0]+=1
count.sort(key=lambda x:x[0])
if(count[-1][0]==count[-2][0]):
    print('?')
else:
    print(count[-1][1])