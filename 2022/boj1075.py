n=int(input())
k=int(input())

ans=k-(n//100*100)%k
if(ans==k):
    print('00')
elif(ans<10):
    print(f"0{ans}")
else:
    print(ans)