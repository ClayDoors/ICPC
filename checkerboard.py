size = int(input())
myArr = []
for _ in range(size):
    myArr.append(input())
for j in range(size):
    zeropls = 0
    for i in range(size):
        if myArr[i][j] == "B":
            zeropls += 1
        else:
            zeropls -= 1
        if((j>0 and j<size-1) and myArr[i][j] == myArr[i][j-1] and myArr[i][j] == myArr[i][j+1]):
            print("0")
            exit()
    if(zeropls != 0):
        print("0")
        break
for i in range(size):
    zeropls = 0
    for j in range(size):
        if myArr[i][j] == "B":
            zeropls += 1
        else:
            zeropls -= 1
        if((i>0 and i<size-1) and myArr[i][j] == myArr[i+1][j] and myArr[i][j] == myArr[i-1][j]):
            print("0")
            exit()
    if(zeropls != 0):
        print("0")
        exit()
print("1")
