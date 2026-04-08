from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for n in tokens:
            if n == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1+val2)
            elif n == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2-val1)
            elif n == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1*val2)
            elif n == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
            else:
                stack.append(int(n))


        return stack[0]