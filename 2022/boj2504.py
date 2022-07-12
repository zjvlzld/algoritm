from collections import deque
get=input()
st=deque()#해당 인풋이 정상인지 확인하기 위한 변수
cal=deque()#인풋 계산을 위한 변수
for i in range(0,len(get)):
    if(get[i]=='['):#st와 cal에 값을 넣어준다
        st.append(get[i])
        cal.append(get[i])
    if(get[i]=='('):#st와 cal에 값을 넣어준다
        st.append(get[i])
        cal.append(get[i])
    if(get[i]==')'):#계산이 일어나야 하는 부분
        if(len(st)==0):#만약 이전에 입력된 값이 없으면
            print(0)#에러처리
            exit()#종료
        if(st[-1]=='('):#직전의 괄호가 짝이 맞는 다면
            st.pop()#해당 괄호 세트는 정상이니 pop
            t=[]#계산을 위해 필요한 저장소
            while(cal[-1]!='('):#이전 짝을 찾기 전까지
                t.append(cal[-1])#안에 있는 수 들을 계산을 위한 저장소에 넣는다
                cal.pop()#해당 수를 cal에서 pop
            cal.pop()#마지막 '('까지 pop
            if(len(t)==0):#만약 괄호 안에 계산할 값이 없으면
                cal.append(2)#2를 넣어준다
            else:#있으면
                cal.append(sum(t)*2)#안에 숫자들을 더한뒤 2를 곱한다
        else:#직전의 괄호가 짝이 안맞으면
            print(0)#오류출력
            exit()#종료
    if(get[i]==']'):#위와 똑같이 동작하나 숫자가 3이 됨
        if(len(st)==0):
            print(0)
            exit()
        if(st[-1]=='['):
            st.pop()
            t=[]
            while(cal[-1]!='['):
                t.append(cal[-1])
                cal.pop()
            cal.pop()
            if(len(t)==0):
                cal.append(3)
            else:
                cal.append(sum(t)*3)

        else:
            print(0)
            exit()
if(len(st)!=0):#만약 )]가 없이 ([가 있는 채로 위 반복문을 빠져 나오면
    print(0)#오류출력
    exit()#종료
print(sum(cal))#cal에 남아있는 숫자를 더하면 정답