from email import policy
import sys
a,b=map(int,sys.stdin.readline().split(" "))
poly=[]
for _ in range(a):
    poly.append([int(x) for x in sys.stdin.readline().split(" ")])

print(poly)