T = int(input())

for t in range(1, T+1):
    get = input()
    minNum = [int(x) for x in get]
    maxNum = [int(x) for x in get]

    for i in range(len(get)):
        if i == 0:
            p = i
            for j in range(len(get)-1, i,-1):
                if minNum[p] > minNum[j] and minNum[j] != 0:
                    p = j
            if p != i:
                minNum[i], minNum[p] = minNum[p], minNum[i]
                break
        else :
            p = i
            for j in range(len(get)-1, i,-1):
                if minNum[p] > minNum[j]:
                    p = j
            if p != i:
                minNum[i], minNum[p] = minNum[p], minNum[i]
                break

    for i in range(len(get)):
        p = i
        for j in range(len(get)-1, i,-1):
            if maxNum[p] < maxNum[j]:
                p = j
        if p != i and maxNum[p] != 0:
            maxNum[i], maxNum[p] = maxNum[p], maxNum[i]
            break
    print('#'+str(t), end=" ")
    for i in minNum:
        print(i, end="")
    print(" ", end="")
    for i in maxNum:
        print(i, end="")
    print()