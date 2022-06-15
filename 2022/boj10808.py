get=input()
ans=[0 for _ in range(26)]
for i in get:
    ans[ord(i)-ord('a')]+=1
for i in ans:
    print(i,end=' ')
print()