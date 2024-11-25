import bisect
class substring:
    def __init__(self,l,u) -> None:
        self.A = [.5,"A"]
        self.G = [.3, "G"]
        self.C = [.2, "C"]
        self.T = [.4, "T"]
        self.lowerLim = l-1
        self.upperLim = u-1
    def __str__(self) -> str:
        nucList = [self.A,self.G,self.C,self.T]
        nucList.sort(key = lambda e: e[0])
        nucList.reverse()
        s=  "".join(nuc[1] for nuc in nucList)
        return s
        #return (str(self.lowerLim) + " " + str(self.upperLim))
        
    
dnastr = input()
numTimes = int(input())
answers = []
substringArr = []
for _ in range(numTimes):
    start,end = map(int, input().split())
    substringArr.append(substring(start,end))
sortedArr = sorted(substringArr,key = lambda string: string.lowerLim)
sortedArr.reverse()
stack = []
for i, char in enumerate(dnastr):
    while sortedArr and sortedArr[-1].lowerLim <= i:
        a = sortedArr.pop()
        bisect.insort(stack,a, key=lambda string: -1 * string.upperLim)
        pass
    while stack and stack[-1].upperLim < i:
        stack.pop()
    if char == "A":
        for s in stack:
            s.A[0] += 1
            pass
        continue
    elif char == "T":
        for s in stack:
            s.T[0] += 1
            pass
        continue
    elif char == "C":
        for s in stack:
            s.C[0] += 1
        continue
    elif char == "G":
        for s in stack:
            s.G[0] += 1
        continue
for sub in substringArr:
    print(str(sub))



'''
TATATGCTCT
3
1 10
6 10
6 6

'''