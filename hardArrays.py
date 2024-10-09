from typing import List
class Solution:
    def findBigger(self, height: List[int]) -> int:
        for i in range(len(height)-2, -1,-1):
            x = height[i]
            y = height[len(height)-1] 
            z = height[i] >= height[len(height)-1]
            if z:
                return i
        return -1

    def findDistance(self, height: List[int]) -> int:
            
            target = self.findBigger(height)
            distance =  len(height)-(target)-2
            if target == -1:
                height[len(height)-1] = height[len(height)-1]-1
                return self.findDistance(height)
            if target == len(height)-2:
                height.pop()
                return 0
            height[len(height)-1] = height[len(height)-1]-1    
            #height[len(height)-1] = height[len(height)-1] - 1
            return distance + self.findDistance(height)

    def trap(self, height: List[int]) -> int:

        while height and height[0] == 0:
            height.pop(0)
        while len(height) > 1 and height[1] > height[0]:
            height.pop(0)
        while len(height) > 1 and height[-1] < height[-2]:
            height.pop()
        #height.append()
        total = 0
        while len(height) > 2:
            total += self.findDistance(height)
        return total
driver = Solution()
print(str(driver.trap([4,2,0,3,2,5])))
