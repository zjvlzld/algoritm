import sys
a,b=map(int,sys.stdin.readline().split(" "))
poly=[]
for _ in range(a):
    poly.append([int(x) for x in sys.stdin.readline().split(" ")])

ans=0
for i in range(a):
    for j in range(b):
        if(i+1<a and j+1<b):
            t=poly[i][j]+poly[i][j+1]+poly[i+1][j]+poly[i+1][j+1]
            if(ans<t):
                ans=t

        if(i+3<a):
            t=poly[i][j]+poly[i+1][j]+poly[i+2][j]+poly[i+3][j]
            if(ans<t):
                ans=t
        if(j+3<b):
            t=poly[i][j]+poly[i][j+1]+poly[i][j+2]+poly[i][j+3]
            if(ans<t):
                ans=t

        if(i+2<a and j+1<b):
            t=0
            t=poly[i][j]+poly[i+1][j]+poly[i+2][j]+poly[i+2][j+1]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i][j+1]+poly[i+1][j+1]+poly[i+2][j+1]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i][j+1]+poly[i+1][j]+poly[i+2][j]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j+1]+poly[i+1][j+1]+poly[i+2][j+1]+poly[i+2][j]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i+1][j]+poly[i+2][j]+poly[i+1][j+1]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j+1]+poly[i+1][j+1]+poly[i+2][j+1]+poly[i+1][j]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i+1][j]+poly[i+1][j+1]+poly[i+2][j+1]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j+1]+poly[i+1][j+1]+poly[i+1][j]+poly[i+2][j]
            if(ans<t):
                ans=t



        if(i+1<a and j+2<b):
            t=0
            t=poly[i][j]+poly[i+1][j]+poly[i+1][j+1]+poly[i+1][j+2]
            if(ans<t):
                ans=t
            t=0
            t=poly[i+1][j]+poly[i][j]+poly[i][j+1]+poly[i][j+2]
            if(ans<t):
                ans=t
            
            t=0
            t=poly[i+1][j]+poly[i+1][j+1]+poly[i+1][j+2]+poly[i][j+2]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i][j+1]+poly[i][j+2]+poly[i+1][j+2]
            if(ans<t):
                ans=t
            
            t=0
            t=poly[i][j+1]+poly[i+1][j]+poly[i+1][j+1]+poly[i+1][j+2]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i][j+1]+poly[i][j+2]+poly[i+1][j+1]
            if(ans<t):
                ans=t
            
            t=0
            t=poly[i+1][j]+poly[i+1][j+1]+poly[i][j+1]+poly[i][j+2]
            if(ans<t):
                ans=t
            t=0
            t=poly[i][j]+poly[i][j+1]+poly[i+1][j+1]+poly[i+1][j+2]
            if(ans<t):
                ans=t

print(ans)

