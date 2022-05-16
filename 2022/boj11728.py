import sys

a,b=map(int,sys.stdin.readline().split(" "))

num1=[int(x) for x in sys.stdin.readline().split(" ")]
num2=[int(x) for x in sys.stdin.readline().split(" ")]

i=0
j=0

while(i !=a and j!=b):
    if(num1[i]>=num2[j]):
        print(num2[j],end=' ')
        j+=1
    elif(num1[i]<num2[j]):
        print(num1[i],end=' ')
        i+=1

for q in range(i,a):
    print(num1[q],end=" ")
for k in range(j,b):
    print(num2[k],end=" ")
print()