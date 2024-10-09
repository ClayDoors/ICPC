
#BEATS TRAPPING RAIN WATER



from typing import List
class Solution:
    total = 0
    lowerbound = 0
    def findDistance(self, height: List[int], leftbound, rightbound):
        i = leftbound
        j = rightbound
        mult = 0
        add = 0
        if i == j or j == -1 or i == len(height) or i+1 == j:
            return
        if height[i] > self.lowerbound and height[j] > self.lowerbound:
            mult = min(height[i] - self.lowerbound, height[j] - self.lowerbound)
            add =(( j - i +1 ) * mult)
            totadd = add
            self.total = self.total + totadd
        if height[i] > height[j]:
            j = j -1
        else:
            i = i +1
        self.lowerbound = self.lowerbound + mult
        self.findDistance(height,i,j)
        
        
            




    def trap(self, height: List[int]) -> int:
        
        while height and height[0] == 0:
            height.pop(0)
        while len(height) > 1 and height[1] > height[0]:
            height.pop(0)
        while len(height) > 1 and height[-1] < height[-2]:
            height.pop()
        #height.append()
        if len(height) < 2:
            return 0
        
        self.findDistance(height,0,len(height)-1)
        #height.pop(0)
        #height.pop()
       # print(self.total)
        for i in height:
            if i < self.lowerbound:
               # print(self.total)
                self.total = self.total - i
            else:
               # print(self.total)
                self.total = self.total - self.lowerbound
        return self.total
driver = Solution()
print(str(driver.trap([5,4,1,2])))