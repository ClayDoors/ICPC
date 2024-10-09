responses = []
def readBoard():
    row1 = input()
    row2 = input()
    row3 = input()
    aR = row1+row2+row3
    rows = list(aR)
    xcount = 0
    ocount = 0
    if len(rows) != 9:
        responses.append("no")
    for let in rows:
        if let == "X":
            xcount += 1
        if let == "O":
            ocount += 1
    if xcount == ocount + 1 or xcount == ocount:
        responses.append("yes")
    else:
        responses.append("no")
numTimes = int(input())
for i in range(numTimes-1):
    readBoard()
    input()
readBoard()
for word in responses:
    print(word)
    
