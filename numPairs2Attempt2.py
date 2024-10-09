from typing import List


class Solution:
    lF = -1
    lFL = []
    def findFactors(self,n):
        if n == self.lF:
            return self.lFL
        self.lF = n
        factors = []
        i = 1
        j = n
        while True:
            if i*j == n:
                factors.append(i)
                if i == j:
                    break
                factors.append(j)
            i += 1
            j = n // i
            if i > j:
                break
        self.lFL = factors
        return factors
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums3 = {}
        nums4 = {}
        for num in nums1:
            factors = self.findFactors(num)
            for fact in factors:
                if fact%k == 0:
                    if fact/k not in nums3:
                        nums3[fact/k] = 1
                    else:
                        nums3[fact/k] = nums3[fact/k] + 1
        counter = 0
        for num in nums2:
            if num in nums4:
                nums4[num] += 1
            else:
                nums4[num] = 1
        for num in nums4:
            if num in nums3:
                counter = counter + (nums3[num] * nums4[num])
        return counter
        