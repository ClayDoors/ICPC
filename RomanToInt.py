class Solution:
    def romanToInt(self, s: str) -> int:
        myDict = {
            'I' : (1,1),
            'V' : (5,2),
            'X' : (10,3),
            'L' : (50,4),
            'C' : (100,5),
            'D' : (500,6),
            'M' : (1000,7)
        }
        counter = 0
        size = 8

        for i in range(len(s)):
            if myDict[s[i]][1] <= size and (i==len(s)-1 or myDict[s[i][0]] >= myDict[s[i+1][0]]):
                counter = counter + myDict[s[i]][0]
                size = myDict[s[i]][1]
            else:
                counter = counter - myDict[s[i]][0]
        return counter
d = Solution()
print(str(d.romanToInt("III")))