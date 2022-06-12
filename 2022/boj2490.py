for _ in range(3):
    nums=[int(x) for x in input().split(' ')]
    if(sum(nums)==0):
        print('D')
    if(sum(nums)==1):
        print('C')
    if(sum(nums)==2):
        print('B')
    if(sum(nums)==3):
        print('A')
    if(sum(nums)==4):
        print('E')
    
    
    