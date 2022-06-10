n=int(input())
count=[0 for _ in range(26)]
for _ in range(n):
    count[ord(input()[0])-ord('a')]+=1

ans=""
for i in range(26):
    if count[i]>=5:
        ans+=str(chr(i+ord('a')))

if len(ans)==0:
    print('PREDAJA')
else:
    print(ans)
