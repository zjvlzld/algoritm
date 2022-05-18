import sys
from collections import deque

T = int(sys.stdin.readline())

que = deque()

for _ in range(T):
    get = sys.stdin.readline()
    if get[:4] == 'push':
        que.append(int(get[5:-1]))
    if get[:3] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    if get[:4] == 'size':
        print(len(que))
    if get[:5] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    if get[:5] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    if get[:4] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
