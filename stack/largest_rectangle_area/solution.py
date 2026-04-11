from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []

        area = 0

        for i in range(len(heights)):
            
            index = i

            while stack and heights[i] < stack[-1][1]:                
                j,h = stack.pop()
                area = max(area, h * (i - j))
                index = j

            stack.append([index,heights[i]])

    
        for i in range(len(stack)):
            area = max(area, stack[i][1] * (len(heights) - stack[i][0]))

        return area