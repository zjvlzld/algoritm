import sys
n=int(sys.stdin.readline())
nums=[int(x) for x in sys.stdin.readline().split(" ")]

counts=[int(x) for x in sys.stdin.readline().split(" ")]
cal=[]
for i in range(4):
    for j in range(counts[i]):
        cal.append(i)
ans=[]
def sol(before,now,que):
    if(len(que)==0):
        ans.append(before)
        return
    for i in range(len(que)):
        if(que[i]==0):
            que.pop(i)
            sol(before+nums[now],now+1,que)
            que.insert(i,0)
        if(que[i]==1):
            que.pop(i)
            sol(before-nums[now],now+1,que)
            que.insert(i,1)
        if(que[i]==2):
            que.pop(i)
            sol(before*nums[now],now+1,que)
            que.insert(i,2)
        if(que[i]==3):
            que.pop(i)
            if(before<0):
                before=-1*(before*-1//nums[now])
                sol(before,now+1,que)
            else:
                sol(before//nums[now],now+1,que)
            que.insert(i,3)
sol(nums[0],1,cal)
ans.sort()
print(ans[-1])
print(ans[0])
        