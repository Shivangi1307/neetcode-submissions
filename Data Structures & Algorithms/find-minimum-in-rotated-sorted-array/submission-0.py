class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        index = 0

        while left < right:
            
            mid = left + (right - left) // 2

            if nums[left] <= nums[mid] >= nums[right]:
                left = mid + 1
            elif nums[left >= nums[mid] <= nums[right]]:
                right = mid

        return nums[left]
