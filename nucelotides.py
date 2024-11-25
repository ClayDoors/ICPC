dnastr = input()
numTimes = int(input())
answers = []
for _ in range(numTimes):
    start,end = map(int, input().split())
    ansList = []
    myDict = {
        "A" : .5,
        "G" : .3,
        "C" : .2,
        "T" : .4
    }
    for ch in dnastr[start-1:end]:
        myDict[ch] += 1
    for key in myDict:
        ansList.append((myDict[key],key))
    ansList.sort()
    ansList.reverse()
    finalstr = "".join(ans[1] for ans in ansList)
    answers.append(finalstr)
for ans in answers:
    print(ans)