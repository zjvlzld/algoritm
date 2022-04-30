T=int(input())
q1=q2=q3=q4=axis=0

for _ in range(T):
    x,y=map(int,input().split())
    if(x==0 or y==0):
        axis+=1
    else:
        if(x<0):
            if(y<0):
                q3+=1
            else:
                q2+=1
        else:
            if(y<0):
                q4+=1
            else:
                q1+=1
print('Q1:',q1)
print('Q2:',q2)
print('Q3:',q3)
print('Q4:',q4)
print('AXIS:',axis)