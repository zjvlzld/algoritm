a,b=input().split(' ')
ra=''
rb=''
for i in a:
    ra=i+ra
for i in b:
    rb=i+rb
t=int(ra)+int(rb)
t=str(t)
rt=''
for i in t:
    rt=i+rt
print(int(rt))