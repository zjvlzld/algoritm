get=int(input())

if(get%10!=0):
    print(-1)
else:
    print(get//300,(get%300)//60,((get%60)//10))
