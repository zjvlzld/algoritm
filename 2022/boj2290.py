import sys

s,num=sys.stdin.readline().split(" ")
s=int(s)
nums=[int(num[i]) for i in range(len(num)-1)]

pan=[[' 'for _ in range((s+3)*len(nums)-1)]for _ in range(2*s+3)]

for i in range(len(nums)):
    x=(s+2)*i+i
    y=0

    if(nums[i]==0):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x]='|'
            pan[1+j][x+s+1]='|'
            pan[s+2+j][x]='|'
            pan[s+2+j][x+s+1]='|'
            pan[2*s+2][x+1+j]='-'

    if(nums[i]==1):
        for j in range(s):
            pan[1+j][x+s+1]='|'
            pan[s+2+j][x+s+1]='|'

    if(nums[i]==2):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x+s+1]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x]='|'
            pan[2*s+2][x+1+j]='-'

    if(nums[i]==3):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x+s+1]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x+s+1]='|'
            pan[2*s+2][x+1+j]='-'

    if(nums[i]==4):
        for j in range(s):
            pan[1+j][x]='|'
            pan[1+j][x+s+1]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x+s+1]='|'
   
    if(nums[i]==5):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x+s+1]='|'
            pan[2*s+2][x+1+j]='-'

    if(nums[i]==6):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x]='|'
            pan[s+2+j][x+s+1]='|'
            pan[2*s+2][x+1+j]='-'

    if(nums[i]==7):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x+s+1]='|'
            pan[s+2+j][x+s+1]='|'

    if(nums[i]==8):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x]='|'
            pan[1+j][x+s+1]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x]='|'
            pan[s+2+j][x+s+1]='|'
            pan[2*s+2][x+1+j]='-'
    if(nums[i]==9):
        for j in range(s):
            pan[0][x+1+j]='-'
            pan[1+j][x]='|'
            pan[1+j][x+s+1]='|'
            pan[s+1][x+1+j]='-'
            pan[s+2+j][x+s+1]='|'
            pan[2*s+2][x+1+j]='-'

for i in range(2*s+3):
    for j in range((s+3)*len(nums)-1):
        print(pan[i][j],end="")
    print()
