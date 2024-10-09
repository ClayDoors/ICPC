from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            minus = target - nums[i]
            if minus in dict:
                return [dict[minus],i]
            dict[nums[i]] = i
            pass
driver = Solution()
print(str(driver.twoSum([3,2,4],6)))