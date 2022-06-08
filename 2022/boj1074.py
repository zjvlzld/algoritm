N,x,y=map(int,input().split(" "))

m=[[0 for _ in range(1024)]for _ in range(1024)]

i=0
while i<N:
    t=2**i
    for i in range(t):
        for j in range(t):
            m[i][t+j]=m[i][j]+t*t
    for i in range(t):
        for j in range(t):
            m[i+t][j]=m[i][j]+2*t*t
    for i in range(t):
        for j in range(t):
            m[i+t][j+t]=m[i][j]+3*t*t
    i+=1
print(m)
print(m[x][y])