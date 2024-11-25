import bisect
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()

        for i in range(k):
            a = gifts.pop()
            b = int(math.sqrt(a))
            bisect.insort(gifts,b)
            pass
        return sum(gifts)
driver = Solution()
print(str(driver.pickGifts([25,64,9,4,100],4)))