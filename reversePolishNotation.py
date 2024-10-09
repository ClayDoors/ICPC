from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        counter = 0
        if len(tokens) == 1:
            return int(tokens[0])
        latestOp = False
        for ch in tokens:
            if not (ch == "*" or ch == "/" or ch == "-" or ch == "+"):
                nums.append((int(ch)))
            if True:
                if ch == "*":
                    x = nums.pop()
                    y = nums.pop()
                    counter = x * y
                    nums.append(counter)
                elif ch == "+":

                    x = nums.pop()
                    y = nums.pop()
                    counter = x + y
                    nums.append(counter)
                elif ch == "-":
                    x = nums.pop()
                    y = nums.pop()
                    counter = y - x
                    nums.append(counter)
                elif ch == "/":
                     x = nums.pop()
                     y = nums.pop()
                     counter = int(y/x)
                     nums.append(counter)
        return nums.pop()
driver = Solution()
print(str(driver.evalRPN(["3","11","+","5","-"])))