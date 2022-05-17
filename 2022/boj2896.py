import sys

a,b,c=map(int,sys.stdin.readline().split(" "))
x,y,z=map(int,sys.stdin.readline().split(" "))

sub=min(a/x,b/y,c/z)

print(a-x*sub,b-y*sub,c-z*sub)