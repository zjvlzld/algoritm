
a,b=input().split(" ")

carry=0
ans=''
if(len(a)<len(b)):
    t=a
    a=b
    b=t
for i in range(1,len(b)+1):
    ans=str((int(a[len(a)-i])+int(b[len(b)-i])+carry)%10)+ans
    carry=(int(a[len(a)-i])+int(b[len(b)-i])+carry)//10
for i in range(len(b)+1,len(a)+1):
    ans=str((int(a[len(a)-i])+carry)%10)+ans
    carry=(int(a[len(a)-i])+carry)//10
if(carry!=0):
    print('1'+ans)
else:
    print(ans)