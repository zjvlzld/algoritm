gets=[int(x) for x in input().split()]

gets.sort()
if(gets[0]==gets[1] and gets[1]==gets[2]):
    print(10000+gets[0]*1000)
elif(gets[0]==gets[1]):
    print(1000+100*gets[0])
elif(gets[1]==gets[2]):
    print(1000+100*gets[1])
else:
    print(100*gets[2])