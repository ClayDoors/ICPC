from collections import defaultdict


nums = [1,2,3,4,4,4,4]
count = defaultdict(int)
for i in range(len(nums)):
    count[i] = nums[i]


