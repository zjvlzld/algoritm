import sys
n,l=map(int,sys.stdin.readline().split(" "))

m=[]
for _ in range(n):
    m.append([int(x) for x in sys.stdin.readline().split(" ")])
ans=0
for i in range(n):
    used=[0 for _ in range(n)]
    check=True
    for j in range(n-1):
        if(m[i][j]<m[i][j+1]):
            if(m[i][j+1]-m[i][j]>1):
                check=False
                break
            
            check2=False
            for k in range(l):
                if(j-k<0 or m[i][j]!=m[i][j-k] or used[j-k]==1):
                    check2=True
                    break
            if(check2):
                check=False
                break
            for k in range(l):
                used[j-k]=1
                
        if(m[i][j]>m[i][j+1]):
            if(m[i][j]-m[i][j+1]>1):
                check=False
                break

            check2=False
            for k in range(1,l+1):
                if(j+k>n-1 or m[i][j+1]!=m[i][j+k] or used[j+k]==1):
                    check2=True
                    break
            if(check2):
                check=False
                break
            for k in range(1,l+1):
                used[j+k]=1
            j+=l
    if(check):
        ans+=1
for i in range(n):
    used=[0 for _ in range(n)]
    check=True
    for j in range(n-1):
        if(m[j][i]<m[j+1][i]):
            if(m[j+1][i]-m[j][i]>1):
                check=False
                break
            
            check2=False
            for k in range(l):
                if(j-k<0 or m[j][i]!=m[j-k][i] or used[j-k]==1):
                    check2=True
                    break
            if(check2):
                check=False
                break
            for k in range(l):
                used[j-k]=1
                
        if(m[j][i]>m[j+1][i]):
            if(m[j][i]-m[j+1][i]>1):
                check=False
                break

            check2=False
            for k in range(1,l+1):
                if(j+k>n-1 or m[j+1][i]!=m[j+k][i] or used[j+k]==1):
                    check2=True
                    break
            if(check2):
                check=False
                break
            for k in range(1,l+1):
                used[j+k]=1
            j+=l
    if(check):
        ans+=1
print(ans)                
        
            