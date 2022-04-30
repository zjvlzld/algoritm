from pickle import FALSE


T=int(input())
ans=0
for t in range(T):
    count=[-1 for _ in range(26)]
    getWord=input()
    check=0
    for i in range(len(getWord)) :
        if(count[ord(getWord[i])-97]==-1):
            count[ord(getWord[i])-97]=i
        elif(count[ord(getWord[i])-97]==i-1):
            count[ord(getWord[i])-97]=i
        else:
            check=1
            break
    if(check==0):
        ans+=1

print(ans)