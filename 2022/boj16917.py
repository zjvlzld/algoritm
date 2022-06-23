get=list(int(x) for x in input().split(' '))
ans=0
if(get[0]+get[1]>get[2]*2):
    ans=get[2]*2*min(get[3],get[4])
    if(get[0]<get[2]*2):
        ans+=get[0]*(get[3]-min(get[3],get[4]))
    else:
        ans+=get[2]*2*(get[3]-min(get[3],get[4]))
    if(get[1]<get[2]*2):
        ans+=get[1]*(get[4]-min(get[3],get[4]))
    else:
        ans+=get[2]*2*(get[4]-min(get[3],get[4]))
else:
    ans=get[0]*get[3]+get[1]*get[4]
print(ans)