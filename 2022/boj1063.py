k,s,n=input().split()

nowK=[ord(k[0])-ord('A'),int(k[1])-1]
nowS=[ord(s[0])-ord('A'),int(s[1])-1]

print(nowK,nowS)

for _ in range(int(n)):
    print(f"{chr(ord('A')+nowK[0])}{nowK[1]+1} {chr(ord('A')+nowS[0])}{nowS[1]+1}")
    get=input()
    if(get=='R'):
        if(nowK[0]+1>=8):
            continue
        if(nowK[0]+1==nowS[0] and nowK[1]==nowS[1]):
            if(nowS[0]+1>=8):
                continue
            else:
                nowK=[nowK[0]+1,nowK[1]]
                nowS=[nowS[0]+1,nowS[1]]
                continue
        nowK=[nowK[0]+1,nowK[1]]
    elif(get=='L'):
        if(nowK[0]-1<0):
            continue
        if(nowK[0]-1==nowS[0] and nowK[1]==nowS[1]):
            if(nowS[0]-1<0):
                continue
            else:
                nowK=[nowK[0]-1,nowK[1]]
                nowS=[nowS[0]-1,nowS[1]]
                continue
        nowK=[nowK[0]-1,nowK[1]]

    elif(get=='T'):
        if(nowK[1]+1>=8):
            continue
        if(nowK[1]+1==nowS[1] and nowK[0]==nowS[0]):
            if(nowS[1]+1>=8):
                continue
            else:
                nowK=[nowK[0],nowK[1]+1]
                nowS=[nowS[0],nowS[1]+1]
                continue
        nowK=[nowK[0],nowK[1]+1]

    elif(get=='B'):
        if(nowK[1]-1<0):
            continue
        if(nowK[1]-1==nowS[1] and nowK[0]==nowS[0]):
            if(nowS[1]-1<0):
                continue
            else:
                nowK=[nowK[0],nowK[1]-1]
                nowS=[nowS[0],nowS[1]-1]
                continue
        nowK=[nowK[0],nowK[1]-1]


    elif(get=='RT'):
        if(nowK[0]+1>=8 or nowK[1]+1>=8):
            continue
        if(nowK[0]+1==nowS[0] and nowK[1]+1==nowS[1]):
            if(nowS[0]+1>=8 or nowS[1]+1>=8):
                continue
            else:
                nowK=[nowK[0]+1,nowK[1]+1]
                nowS=[nowS[0]+1,nowS[1]+1]
                continue
        nowK=[nowK[0]+1,nowK[1]+1]
    
    elif(get=='RB'):
        if(nowK[0]+1>=8 or nowK[1]-1<0):
            continue
        if(nowK[0]+1==nowS[0] and nowK[1]-1==nowS[1]):
            if(nowS[0]+1>=8 or nowS[1]-1<0):
                continue
            else:
                nowK=[nowK[0]+1,nowK[1]-1]
                nowS=[nowS[0]+1,nowS[1]-1]
                continue
        nowK=[nowK[0]+1,nowK[1]-1]
    
    elif(get=='LB'):
        if(nowK[0]-1<0 or nowK[1]-1<0):
            continue
        if(nowK[0]-1==nowS[0] and nowK[1]-1==nowS[1]):
            if(nowS[0]-1<0 or nowS[1]-1<0):
                continue
            else:
                nowK=[nowK[0]-1,nowK[1]-1]
                nowS=[nowS[0]-1,nowS[1]-1]
                continue
        nowK=[nowK[0]-1,nowK[1]-1]

    elif(get=='LT'):
        if(nowK[0]-1<0 or nowK[1]+1>=8):
            continue
        if(nowK[0]-1==nowS[0] and nowK[1]+1==nowS[1]):
            if(nowS[0]-1<0 or nowS[1]+1>=8):
                continue
            else:
                nowK=[nowK[0]-1,nowK[1]+1]
                nowS=[nowS[0]-1,nowS[1]+1]
                continue
        nowK=[nowK[0]-1,nowK[1]+1]

print(f"{chr(ord('A')+nowK[0])}{nowK[1]+1}\n{chr(ord('A')+nowS[0])}{nowS[1]+1}")
