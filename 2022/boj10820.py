get=input()
s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in get:
    if i in s:
        print(s[((ord(i)-ord('a'))+13)%26],end="")
    elif i in l:
        print(l[((ord(i)-ord('A'))+13)%26],end="")

    else:
        print(i,end="")