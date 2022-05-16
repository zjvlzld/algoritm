import sys


cal={0:1}

n,p,q=map(int, sys.stdin.readline().split(" "))

def get(now):
    if cal.get(now)!=None:
        return cal.get(now)
    else:

        cal[now]=get(now//p)+get(now//q)
        return cal[now]
print(get(n))