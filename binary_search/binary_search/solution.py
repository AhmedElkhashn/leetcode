from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:

            midpoint = l + (( r - l ) // 2)

            if target > nums[midpoint]:
                l = midpoint + 1
            elif target < nums[midpoint]:
                r = midpoint - 1
            else:
                return midpoint


        return -1