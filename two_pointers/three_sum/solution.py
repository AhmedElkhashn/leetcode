from typing import List


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        output = []
        

        for i, n in enumerate(nums):

            if i > 0 and n == nums[i - 1]:
                continue

            j,k = i + 1, len(nums) - 1

            while j < k:
                sum  = n + nums[j] + nums[k] 

                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1 
                else:
                    output.append([n,nums[j],nums[k]])  
                    j += 1
                    while nums[j] == nums [j - 1] and j < k:
                        j += 1

        return output
  