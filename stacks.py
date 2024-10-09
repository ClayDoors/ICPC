class Solution:
    def removeDuplicates(self, s: str) -> str:
        lastLet = "."
        st = list(s)
        a = 0
        while a < len(st):
            if st[a] == lastLet:
               # print("hi")
                st.pop(a-1)
                st.pop(a-1)
                a -= 2
                lastLet = "."
                return self.removeDuplicates(st)
            else:
                
                lastLet = st[a]
                a += 1
        finalWord = ""
        for c in st:
            finalWord += c
        return finalWord
        
s = Solution()
print(s.removeDuplicates("abbaca"))