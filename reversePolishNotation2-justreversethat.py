from typing import List


class Solution:
    def eval(self,tokens: List[str],i) -> int:
        op = tokens[i]
        for i in range(2):
            if
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = reversed(tokens)
        return eval(tokens,0)
driver = Solution()
print(str(driver.evalRPN(["3","11","+","5","-"])))