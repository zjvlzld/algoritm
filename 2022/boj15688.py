import sys
n = []
N = int(sys.stdin.readline())

for _ in range(N):
    n.append(int(sys.stdin.readline()))

n.sort()

for i in n:
    print(i)
