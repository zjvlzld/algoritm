import sys
import copy
pan=[]

n,T=map(int,sys.stdin.readline().split(" "))

for _ in range(2**n):
    pan.append([int(x) for x in sys.stdin.readline().split(" ")])

for _ in range(T):
    a,b=map(int,sys.stdin.readline().split(" "))
    temp=copy.deepcopy(pan)

    if(a==1):
        for i in range(2**(n-b)):
            for j in range(2**(n-b)):
                for k in range((2**b)//2):
                    for q in range(2**b):
                        t=temp[2**b*i+k][2**b*j+q]   
                        pan[2**b*i+k][2**b*j+q]=temp[2**b*(i+1)-1-k][2**b*j+q]
                        pan[2**b*(i+1)-1-k][2**b*j+q]=t
    if(a==2):
        for i in range(2**(n-b)):
            for j in range(2**(n-b)):
                for k in range((2**b)):
                    for q in range((2**b)//2):
                        t=temp[2**b*i+k][2**b*j+q]   
                        pan[2**b*i+k][2**b*j+q]=temp[2**b*(i)+k][2**b*(j+1)-1-q]
                        pan[2**b*(i)+k][2**b*(j+1)-1-q]=t
    if(a==3):
        for i in range(2**(n-b)):
            for j in range(2**(n-b)):
                for k in range((2**b)):
                    for q in range((2**b)):
                        pan[2**b*i+k][2**b*j+q]=temp[2**b*(i+1)-1-q][2**b*j+k]
    if(a==4):
        for i in range(2**(n-b)):
            for j in range(2**(n-b)):
                for k in range((2**b)):
                    for q in range((2**b)):
                        pan[2**b*i+k][2**b*j+q]=temp[2**b*(i)+q][2**b*(j+1)-1-k]

    for s in pan:
        for w in s:
            print(w,end=" ")
        print()