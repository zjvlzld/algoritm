gets=[0,0]

input()
get=input()

for i in range(len(get)):
    gets[ord(get[i])-65]+=1

if(gets[0]==gets[1]):
    print('Tie')
elif(gets[0]<gets[1]):
    print('B')
else:
    print('A')