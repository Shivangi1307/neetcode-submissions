from math import inf
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window = []
        min_elements = inf

        if sum(nums) < target:
            return 0
            
        for right in range(len(nums)):
            total = sum(nums[left:right+1])

            while  total >= target:
                min_elements = min(min_elements,len(nums[left:right+1]))
                left += 1
                total = sum(nums[left:right+1])
            


        return min_elements