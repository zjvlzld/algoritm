N,y,x=map(int,input().split(" "))


def solution(add,s,sx,sy):
    if(s==1):
        print(add)
        exit()
    s=s//2
    if(sx<=x<sx+s and sy<=y<sy+s):
        solution(add,s,sx,sy)
    if(sx+s<=x and sy<=y<sy+s):
        solution(add+s*s,s,sx+s,sy)
    if(sx<=x<sx+s and sy+s<=y):
        solution(add+s*s*2,s,sx,sy+s)
    if(sx+s<=x and sy+s<=y):
        solution(add+s*s*3,s,sx+s,sy+s)

solution(0,2**N,0,0)