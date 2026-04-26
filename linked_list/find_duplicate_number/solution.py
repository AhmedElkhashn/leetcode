from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        i, j, k = 0, 0, 0

        while True:

            i = nums[i]
            j = nums[nums[j]]

            if i == j:
                break

        while True:

            i = nums[i]
            k = nums[k]

            if i == k:
                return k 
        