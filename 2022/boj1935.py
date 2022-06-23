n=int(input())
get=input()
nums=[]
for _ in range(n):
    nums.append(int(input()))
st=[]
cal=['+','-','/','*','%']
for i in get:
    if i in cal:
        if i =='+':
            t=st[-1]+st[-2]
            st.pop(-1)
            st.pop(-1)
            st.append(t)
        if i =='-':
            t=st[-2]-st[-1]
            st.pop(-1)
            st.pop(-1)
            st.append(t)
        if i =='/':
            t=st[-2]/st[-1]
            st.pop(-1)
            st.pop(-1)
            st.append(t)
        if i =='*':
            t=st[-1]*st[-2]
            st.pop(-1)
            st.pop(-1)
            st.append(t)
        if i =='%':
            t=st[-2]%st[-1]
            st.pop(-1)
            st.pop(-1)
            st.append(t)
    else:
        st.append(nums[ord(i)-ord('A')])
print("{:.2f}".format(st[0]))