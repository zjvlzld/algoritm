from collections import deque
n=int(input())

card=[x for x in range(1,n+1)]
d=deque()
for i in range(1,n+1):
    d.append(i)

while(len(d)!=1):
    d.popleft()
    d.append(d.popleft())

print(d[0])