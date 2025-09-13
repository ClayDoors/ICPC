from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        seenQueue = deque()
        count = 0
        biggestCount = 0
        for ch in s:
            if ch not in seen:
                seen.add(ch)
                count+=1
                if count > biggestCount:
                    pass
                    biggestCount = count
                seenQueue.append(ch)
            else:
                for i in range(count):
                    count-=1
                    myChar = seenQueue.popleft()
                    seen.remove(myChar)
                    if myChar == ch:
                        pass
                        seen.add(ch)
                        seenQueue.append(ch)
                        count+=1
                        break
        return biggestCount
h = Solution()
print(h.lengthOfLongestSubstring("pwwkew"))