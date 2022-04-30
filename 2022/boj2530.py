st,sm,ss=[int(x) for x in input().split(" ")]
get= int(input())

gett=get//3600
getm=(get//60)%60
gets=get%60
print(gett,getm,gets)

anss=(ss+gets)%60
carry=(ss+gets)//60

ansm=(sm+getm+carry)%60
carry=(sm+getm+carry)//60

anst=(st+gett+carry)%24

print(anst,ansm,anss)
