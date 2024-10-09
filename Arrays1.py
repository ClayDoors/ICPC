numWords = int(input())
words = set()
turnPlayer1 = False
lose = False
list = []
currentWord = ""
lastWord = ""
for _ in range(numWords):
    list.append(input())
#print(list)
lastWord = list[0]
words.add(lastWord)
#print(words)
for i in range(1,numWords):
    turnPlayer1 = not turnPlayer1
    
    currentWord = list[i]
    if currentWord[0] != lastWord[-1]:
        #print("Do it")
        lose = True
        break
    if currentWord in words:
       # print("hi")
        lose = True
        break
    words.add(currentWord)
    lastWord = currentWord
#print(words)
if not lose:
    print("Fair Game")
elif turnPlayer1:
    print("Player 2 Lost")
else:
    print("Player 1 Lost")