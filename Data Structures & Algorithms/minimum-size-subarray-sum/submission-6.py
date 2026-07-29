from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_elements = inf

        if sum(nums) < target:
            return 0
            
        for right in range(len(nums)):
            total += nums[right]

            while  total >= target:
                min_elements = min(min_elements,right - left + 1)
                total -= nums[left]
                left += 1
                

        return 0 if min_elements == inf else min_elements