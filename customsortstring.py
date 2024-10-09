class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sortArr = []
        inSet = set()
        strset = set(s)
        hashmap = {}
        for let in s:
            if let not in hashmap:
                hashmap[let] = 1
            else:
                hashmap[let] += 1
        for i  in range(len(order)):
            if order[i] not in inSet:
                inSet.add(order[i])
                times  = 0
                if order[i] in hashmap:
                    times = hashmap[order[i]]
               
                for _ in range(times):
               
                    sortArr.append((i,order[i]))
        pass
        sortArr.sort()
        finArr = []
        for tupl in sortArr:
            if tupl[1] in strset:
                finArr.append(tupl[1])
        for let in s:
            if let not in inSet:
                finArr.append(let)
        return  ''.join(finArr)
driver = Solution()
print(driver.customSortString("bcafg","abcd"))