####개어렵다 못품
import sys

count=[6,2,5,5,4,5,6,3,7,5]

st=sys.stdin.readline().rstrip()
end=0
for i in range(len(st)):
    end+=count[int(st[i])]
ans=0
while(True):
    ans+=1
    t=st
    carry=0
    c=0
    next=''
    digit = int(st[len(st)-1]) + 1
    if (digit > 9):
        carry = 1
        digit %= 10
    else:
        carry = 0
    c += count[digit]
    next = str(digit) + next
    for i in range(len(st)-2,-1,-1):
        digit=int(st[i])+carry
        if(digit>9):
            carry=1
            digit%=10
        else:
            carry=0
        c+=count[digit]
        next=str(digit)+next
    st=next
    if(c==end):
        print(ans)
        exit()