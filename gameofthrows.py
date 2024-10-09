inputStr = (input()).split()
numCommands = int(inputStr[0])
numKids = int(inputStr[0])
inputStr = (input().split())
commandList = []
flag = False
for i in range(len(inputStr)):
    if flag:
        flag = False
        continue
    if inputStr[i] == "undo":
        for _ in range(int(inputStr[i+1])):
            commandList.pop()
            
            pass
        flag = True
    else:
        num = int(inputStr[i])
        if num<0 :
            x = num%numKids
            commandList.append(numKids- (abs(num)%numKids))
            pass
        else:
            commandList.append(num%numKids)
            pass
#        print("h")
s = sum(commandList)
print(s%numKids)