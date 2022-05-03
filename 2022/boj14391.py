from glob import glob


a,b=map(int,input().split(" "))

nums=[]
for _ in range(a):
    get=input()
    nums.append([int(get[i]) for i in range(len(get))])

visit=[0 for _ in range(a*b)]
ans=0

def cal(now):
    global ans
    global visit
    total=0
    for n in range(a*b):
        if(visit[n]==0 and now[n]==0):
            t=0
            for i in range(n,b-n%b+n):
                if(now[i]==0):
                    visit[i]=1
                    t=t*10+nums[i//b][i%b]
                else:
                    break
            total+=t
        elif(visit[n]==0 and now[n]==1):
            t=0
            for i in range(n,a*b,b):
                if(now[i]==1):
                    visit[i]=1
                    t=t*10+nums[i//b][i%b]
                else:
                    break
            total+=t
    if(total>ans):
        ans=total
    visit=[0 for _ in range(a*b)]
    return

def makeDir(now):
    if(len(now)==a*b):
        cal(now)
        return
    now.append(1)
    makeDir(now)
    now.pop()
    now.append(0)
    makeDir(now)
    now.pop()
    return

makeDir([])
print(ans)