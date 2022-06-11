get=input()
n=[0 for _ in range(10)]
for i in get:
    n[ord(i)-ord('0')]+=1
for i in range(9,-1,-1):
    for _ in range(n[i]):
        print(i,end="")
print()