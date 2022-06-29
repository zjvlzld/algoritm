g=list(int(x) for x in input().split(' '))

while(not (g[1]==0 and g[0]==0 and g[2]==0)):
    g.sort()
    if(g[2]>=g[0]+g[1]):
        print('Invalid')
    elif(g[1]==g[2]==g[0]):
        print('Equilateral')
    elif(g[0]==g[1] or g[1]==g[2] or g[2]==g[1]):
        print('Isosceles')
    else:
        print('Scalene')
    g=list(int(x) for x in input().split(' '))

    