mainStr = input()
totalLength = len(mainStr)
stringset = set()
for i in range (totalLength):
    left = 0
    right = totalLength-i
    while right <= totalLength:
        stringset.add(mainStr[left:right])
        #print(stringset)
        left += 1
        right += 1
print(str(len(stringset)))
    
