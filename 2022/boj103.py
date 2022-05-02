T=int(input())
a=b=100
for _ in range(T):
    g1,g2=map(int,input().split(" "))
    if(g1<g2):
        a-=g2
    if(g1>g2):
        b-=g1
print(a)
print(b)