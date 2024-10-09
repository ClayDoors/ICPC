from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0 
        right = len(people)-1
        counter = 0
        while left <= right:
            if people[left] + people[right] <= limit and right != left:
                left += 1
                right -= 1
                counter += 1
            else:
                right -= 1
                counter += 1
        return counter
driver = Solution()

print(str(driver.numRescueBoats([3,2,2,1],3)))