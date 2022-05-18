import sys

while True :
    get=str(sys.stdin.readline())
    if get[0] == '.':
        break
    st=[]
    for i in range(len(get)):
        check = False
        if get[i] == '(':
            st.append(0)
        if get[i] == ')':
            if len(st) == 0:
                print('no')
                check = True
                break
            if st[-1] != 0:
                print('no')
                check = True
                break
            if st[-1] == 0:
                st.pop()

        if get[i] == '[':
            st.append(1)
        if get[i] == ']':
            if len(st) == 0:
                print('no')
                check = True
                break
            if st[-1] != 1:
                print('no')
                check = True
                break
            if st[-1] == 1:
                st.pop()
    if check:
        continue
    if len(st) == 0:
        print("yes")
    else:
        print("no")