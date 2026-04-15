from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0 
        i, j = 0 , len(height) - 1
        
        while j > i:
            width = j - i
            if height[i] > height[j]:
                length = height[j]
                j -= 1
            else:
                length = height[i]
                i += 1

            area = max(area, length *  width)

        return area