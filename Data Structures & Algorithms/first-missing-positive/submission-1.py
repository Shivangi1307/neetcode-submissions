class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num >=0]
        if not nums:
            return 1
        for num in range(1,max(nums)):
            if num not in nums:
                return num

        return max(nums)+1