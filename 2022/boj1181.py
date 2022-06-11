n=int(input())
word=[]
for _ in range(n):
    word.append(input())
word.sort()
word.sort(key=lambda x:len(x))
print(word[0])
for i in range(1,n):
    if word[i]!=word[i-1]:
        print(word[i])