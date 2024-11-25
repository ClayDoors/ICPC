import heapq
from typing import List

#Try a binary searchy thing
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits = [-x for x in profits]
        heap = []
        for i in range(len(capital)):
            heap.append([capital[i],profits[i]])
        heap.sort()
        foundSet = set()
        profitHashmap = {}

        for i in range(k):
            for i in range(w):
                if heap[i][0] not in foundSet:
                    profitHashmap[heap[i][1]] = i
            temp = max(profitHashmap.keys())
            w += temp
            heap.pop(profitHashmap[temp])
        
            
        return w
