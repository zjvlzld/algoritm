import sys
y,x,my,mx=map(int,sys.stdin.readline().split(" "))

origin=[]

for _ in range(y+my):
    origin.append([int(x) for x in sys.stdin.readline().split(" ")])
for i in range(y-my):
    for j in range(x-mx):
        origin[my+i][mx+j]-=origin[i][j]

for i in range(y):
    for j in range(x):
        print(origin[i][j],end=" ")
    print()