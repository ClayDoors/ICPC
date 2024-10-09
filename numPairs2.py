from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums3 = {}
        nums4 = {}
        for num in nums1:
            if num%k == 0:
                if num/k not in nums3:
                    nums3[num/k] = 1
                else:
                    nums3[num/k] = nums3[num/k] + 1
        for num in nums2:
                if num not in nums4:
                    nums4[num] = 1
                else:
                    nums4[num] = nums4[num] + 1
        counter = 0
        for bigNum in nums3:
            for smallNum in nums4:
                if bigNum%smallNum == 0:
                    counter = counter + (nums3[bigNum] * nums4[smallNum])
        return counter
driver = Solution()
print(driver.numberOfPairs([70,70],[6,10],7))