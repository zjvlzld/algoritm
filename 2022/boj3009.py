from posixpath import split


x=[-1 for _ in range(3)]
y=[-1 for _ in range(3)]

for i in range(3):
    x[i],y[i]=map(int, input().split(" "))

x.sort()
y.sort()
ansx=0
ansy=0
if(x[0]==x[1]):
    ansx=x[2]
else:
    ansx=x[0]

if(y[0]==y[1]):
    ansy=y[2]
else:
    ansy=y[0]

print(ansx,ansy)